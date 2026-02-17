# Hyperliquid Trader Sentiment Analysis

## 📌 Objective
Analyze how market sentiment (Fear/Greed) relates to trader behavior and performance on Hyperliquid.

---

## 📊 Methodology

1. Cleaned and merged sentiment + trader data
2. Aggregated metrics at daily/trader level
3. Compared Fear vs Greed performance
4. Segmented traders by behavior
5. Built simple predictive model

---

## 🔍 Key Insights

- Traders take higher risk on Greed days but PnL consistency drops
- Fear days show lower leverage but more stable win rates
- High-frequency traders perform better in Greed markets

---

## 💡 Strategy Recommendations

1. Reduce leverage during Fear periods
2. Increase trade frequency selectively in Greed markets
3. Risk-manage large position sizes during extreme sentiment

---

## ▶️ How to Run

### Notebook
Open `Hyperliquid_Analysis.ipynb` and run all cells.

### Dashboard (Optional)
```bash
streamlit run app.py
