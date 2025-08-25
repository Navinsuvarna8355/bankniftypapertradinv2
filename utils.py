# utils.py

from datetime import datetime
import pytz
import csv
import os

def get_ist_now():
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist)

def format_ist(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def calculate_pnl(entry, exit, lot_size):
    return round((exit - entry) * lot_size, 2)

def calculate_duration(entry_time, exit_time):
    duration = exit_time - entry_time
    return str(duration)

def log_trade(symbol, signal, entry, exit, lot_size, timeframe, reason, entry_time=None, exit_time=None, file_path='trade_log.csv'):
    entry_time = entry_time or get_ist_now()
    exit_time = exit_time or (entry_time + timedelta(minutes=5))
    timestamp = format_ist(entry_time)
    pnl = calculate_pnl(entry, exit, lot_size)
    duration = calculate_duration(entry_time, exit_time)

    trade_data = {
        'Symbol': symbol,
        'Signal': signal,
        'Entry': entry,
        'Exit': exit,
        'PnL (₹)': pnl,
        'Lot Size': lot_size,
        'Timeframe': timeframe,
        'Timestamp': timestamp,
        'Duration': duration,
        'Reason': reason
    }

    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=trade_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(trade_data)

    return trade_data
