import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from portfolio_analysis import generate_portfolio_plot, get_target_weights_df

st.set_page_config(layout="wide")

# Pie Charts and Additional Image
left_col, right_col = st.columns([2, 1])

with right_col:
    st.title("Portfolio Split Suggestions")
    st.markdown('### Will be updated daily through apache airflow workflow')
    st.markdown("#### Optimal Portfolio Split for Max Returns")
    labels = ['IGLB', 'SPY', 'AMZN']
    sizes = [30, 40, 30]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig1)

    st.markdown("#### Optimal Portfolio Split for Low Risk / Volatility")
    sizes2 = [40, 35, 25]
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes2, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig2)


    st.markdown("#### Target Weights DataFrame")
    st.dataframe(get_target_weights_df())

with left_col:
    st.title("Yesterday Closing Stock Price")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="IGLB", value="$97.35")
    with col2:
        st.metric(label="SPY", value="$412.68")
    with col3:
        st.metric(label="AMZN", value="$129.85")

    st.markdown("---")
    st.subheader("Function Graph")

    st.markdown("#### Portfolio Analysis Plot")
    analysis_plot = generate_portfolio_plot()
    st.pyplot(analysis_plot)

    st.markdown("### Scroll down to see the Data Pipeline & Architecture of the App")

st.markdown("#### My Image")
st.image("https://miro.medium.com/v2/resize:fit:631/1*7jjFg3tGOtsktFnz8yDnHw.jpeg", use_column_width=True)