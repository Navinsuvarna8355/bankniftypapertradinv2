from datetime import datetime
import pytz
import pandas as pd

def get_ist_now():
    """Returns current IST time as datetime object."""
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist)

def format_ist(dt):
    """Formats datetime to readable IST string."""
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def log_trade(symbol, action, price, quantity, pnl, trade_log_path='trade_log.csv'):
    """Appends a trade entry to the CSV log."""
    timestamp = format_ist(get_ist_now())
    entry = {
        'Timestamp (IST)': timestamp,
        'Symbol': symbol,
        'Action': action,
        'Price': price,
        'Quantity': quantity,
        'PnL': pnl
    }
    try:
        df = pd.read_csv(trade_log_path)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([entry])
    df.to_csv(trade_log_path, index=False)
