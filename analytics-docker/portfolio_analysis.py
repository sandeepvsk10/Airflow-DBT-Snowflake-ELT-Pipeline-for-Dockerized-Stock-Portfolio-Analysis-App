import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from dotenv import load_dotenv
import os

import snowflake
from  snowflake.connector import connection

load_dotenv()

conn = snowflake.connector.connect(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    account=os.getenv('ACCOUNT'),
    warehouse=os.getenv('WAREHOUSE'),
    database=os.getenv('DATABASE'),
    schema=os.getenv('SCHEMA')
)

def get_portfolio_data(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM ANALYTICS_TICKER_PRICES")
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
        portfolio_df = pd.DataFrame(data, columns=columns)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise RuntimeError(f"Failed to retrieve : {str(e)}")
    finally:
        cursor.close()
    return portfolio_df

def generate_portfolio_plot():
    portfolio = get_portfolio_data(conn)
    portfolio.set_index(portfolio.columns[0], inplace=True)
    portfolio = portfolio.iloc[::-1]

    logReturns = np.log(portfolio / portfolio.shift(1))
    cumReturns = logReturns.cumsum()

    rng = np.random.default_rng(seed=64)
    portfolio_returns = []
    portfolio_risks = []
    amzn_weights = []
    weights_combination_list = []
    annualization_factor = 260

    for _ in range(10000):
        wts = rng.random(3)
        wts /= np.sum(wts)
        weights_combination_list.append(wts)
        amzn_weights.append(wts[0])
        portfolio_returns.append(annualization_factor * np.dot(wts, logReturns.mean().T)) 
        portfolio_risks.append(np.sqrt(annualization_factor) * np.sqrt(np.dot(np.dot(wts, logReturns.cov()), wts.T)))

    portfolio_returns = np.array(portfolio_returns)
    portfolio_risks = np.array(portfolio_risks)
    amzn_weights = np.array(amzn_weights)

    fig, ax = plt.subplots(figsize=(10,6))
    scatter = ax.scatter(portfolio_risks, portfolio_returns, c=portfolio_returns/portfolio_risks, marker='o', cmap='RdBu', s=10)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=0))
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=0))
    ax.set_title('Return vs Risk for Different Portfolio Weights (Sharpe Ratio Colored)')
    ax.set_xlabel('Portfolio Risk')
    ax.set_ylabel('Portfolio Return')
    fig.colorbar(scatter, label='Sharpe Ratio')

    min_vol_idx = np.argmin(portfolio_risks)
    max_sharpe_idx = np.argmax(portfolio_returns / portfolio_risks)

    ax.plot(portfolio_risks[min_vol_idx], portfolio_returns[min_vol_idx], 'b*', markersize=10, label=f'Min Vol: {portfolio_returns[min_vol_idx]/portfolio_risks[min_vol_idx]:.2f}')
    ax.plot(portfolio_risks[max_sharpe_idx], portfolio_returns[max_sharpe_idx], 'r*', markersize=10, label=f'Max Sharpe: {portfolio_returns[max_sharpe_idx]/portfolio_risks[max_sharpe_idx]:.2f}')
    ax.legend()

    return fig

def get_target_weights_df():
    portfolio = get_portfolio_data(conn)
    portfolio.set_index(portfolio.columns[0], inplace=True)
    portfolio = portfolio.iloc[::-1]

    logReturns = np.log(portfolio / portfolio.shift(1))

    rng = np.random.default_rng(seed=64)
    portfolio_returns = []
    portfolio_risks = []
    weights_combination_list = []
    annualization_factor = 260

    for _ in range(10000):
        wts = rng.random(3)
        wts /= np.sum(wts)
        weights_combination_list.append(wts)
        portfolio_returns.append(annualization_factor * np.dot(wts, logReturns.mean().T)) 
        portfolio_risks.append(np.sqrt(annualization_factor) * np.sqrt(np.dot(np.dot(wts, logReturns.cov()), wts.T)))

    min_vol_idx = np.argmin(portfolio_risks)
    max_sharpe_idx = np.argmax(np.array(portfolio_returns) / np.array(portfolio_risks))

    min_vol_weights = weights_combination_list[min_vol_idx] * 100
    max_sharpe_weights = weights_combination_list[max_sharpe_idx] * 100

    target_weights_df = pd.DataFrame({
        'Security': ['AMZN', 'IGLB', 'SPY'],
        'Min Vol': min_vol_weights,
        'Max Sharpe': max_sharpe_weights
    })

    target_weights_df['Min Vol'] = target_weights_df['Min Vol'].map('{:.2f}%'.format)
    target_weights_df['Max Sharpe'] = target_weights_df['Max Sharpe'].map('{:.2f}%'.format)

    return target_weights_df
