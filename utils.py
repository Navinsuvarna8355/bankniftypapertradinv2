# app.py

import streamlit as st
import pandas as pd
from datetime import timedelta
from utils import log_trade, get_ist_now, format_ist
import os

st.set_page_config(page_title="Auto Paper Trading Dashboard", layout="wide")
st.title("📈 NIFTY/BANKNIFTY Paper Trading")
st.caption(f"🕒 {format_ist(get_ist_now())} IST")

# --- Trade Input Panel ---
with st.sidebar:
    st.header("🛠 Trade Setup")
    symbol = st.selectbox("Symbol", ["NIFTY", "BANKNIFTY"])
    signal = st.selectbox("Signal", ["BUY", "SELL"])
    entry = st.number_input("Entry Price", value=24870.25)
    exit = st.number_input("Exit Price", value=24910.25)
    lot_size = st.number_input("Lot Size", value=75)
    timeframe = st.selectbox("Timeframe", ["5m", "15m", "1h"])
    reason = st.text_input("Signal Reason", value="Close > EMA (bullish)")

    entry_time = get_ist_now()
    exit_time = entry_time + timedelta(minutes=5)

    if st.button("Log Trade"):
        trade = log_trade(
            symbol=symbol,
            signal=signal,
            entry=entry,
            exit=exit,
            lot_size=lot_size,
            timeframe=timeframe,
            reason=reason,
            entry_time=entry_time,
            exit_time=exit_time
        )
        st.success(f"✅ Trade logged: {trade['Symbol']} {trade['Signal']} @ {trade['Timestamp']}")

# --- Trade Log Panel ---
st.subheader("📄 Trade Log")
if os.path.exists("trade_log.csv"):
    df = pd.read_csv("trade_log.csv")
    st.dataframe(df, use_container_width=True)
    st.download_button("Download CSV", df.to_csv(index=False), "trade_log.csv")
else:
    st.info("No trades logged yet.")
