import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("final_data.csv")

st.title("📊 Hyperliquid Trader Sentiment Dashboard")

st.write("Fear vs Greed Analysis")

# Trade count
st.subheader("Trade Count by Sentiment")
st.bar_chart(data['classification'].value_counts())

# Avg PnL
st.subheader("Average PnL by Sentiment")
avg_pnl = data.groupby('classification')['closed pnl'].mean()
st.bar_chart(avg_pnl)

# PnL distribution
st.subheader("PnL Distribution")

fig, ax = plt.subplots()
ax.hist(data['closed pnl'], bins=30)
st.pyplot(fig)

# Data preview
st.subheader("Raw Data")
st.dataframe(data.head(50))
