import MetaTrader5 as mt5
import pandas as pd


if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Analiz yapılacak sembol ve zaman dilimi
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_H1

# Son 100 mumu
try:
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)
except Exception as e:
    print(f"Veri çekme hatası: {e}")
    mt5.shutdown()
    quit()


# Pandas DataFrame'e dönüştür
df = pd.DataFrame(rates)
# Zaman sütununu okunabilir formata çevir
df['time'] = pd.to_datetime(df['time'], unit='s')

print(f"{symbol} için son 5 mum verisi:")
print(df.tail(5))

# (SMA) hes
sma_period = 20
df['sma'] = df['close'].rolling(window=sma_period).mean()

print(f"\n{sma_period} periyotluk SMA ile birlikte son 5 veri:")
print(df.tail(5))


mt5.shutdown()
