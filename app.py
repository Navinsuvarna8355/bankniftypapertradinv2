import streamlit as st
from utils import log_trade, get_ist_now, format_ist

st.set_page_config(page_title="BankNIFTY/NIFTY Paper Trading", layout="wide")

st.title("📊 Dual-Symbol Paper Trading Dashboard")
st.caption(f"Live IST Time: {format_ist(get_ist_now())}")

# --- Trade Input Panel ---
st.sidebar.header("Trade Input")
symbol = st.sidebar.selectbox("Symbol", ["NIFTY", "BANKNIFTY"])
action = st.sidebar.selectbox("Action", ["Buy", "Sell"])
price = st.sidebar.number_input("Price", min_value=0.0, format="%.2f")
quantity = st.sidebar.number_input("Quantity", min_value=1, step=1)
pnl = st.sidebar.number_input("PnL", format="%.2f")

if st.sidebar.button("Log Trade"):
    log_trade(symbol, action, price, quantity, pnl)
    st.sidebar.success("Trade logged successfully!")

# --- Trade Log Viewer ---
st.subheader("📁 Trade Log")
try:
    import pandas as pd
    df = pd.read_csv("trade_log.csv")
    st.dataframe(df)
    st.download_button("Download CSV", df.to_csv(index=False), "trade_log.csv", "text/csv")
except FileNotFoundError:
    st.warning("No trades logged yet.")
