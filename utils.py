# utils.py

from datetime import datetime
import pytz
import csv
import os

def get_ist_timestamp():
    try:
        ist = pytz.timezone('Asia/Kolkata')
        return datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')  # Fallback to UTC

def calculate_pnl(entry, exit, lot_size):
    return round((exit - entry) * lot_size, 2)

def calculate_duration(entry_time, exit_time):
    duration = exit_time - entry_time
    return str(duration)

def log_trade(symbol, signal, entry, exit, lot_size, timeframe, reason, entry_time=None, exit_time=None, file_path='trade_log.csv'):
    timestamp = get_ist_timestamp()
    pnl = calculate_pnl(entry, exit, lot_size)
    duration = calculate_duration(entry_time, exit_time) if entry_time and exit_time else 'NA'

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

