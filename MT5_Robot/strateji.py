import MetaTrader5 as mt5
import pandas as pd


if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_H1
sma_period = 20

rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)
df = pd.DataFrame(rates)
df['sma'] = df['close'].rolling(window=sma_period).mean()

# Analiz için en son tamamlanmış mumu kullanırız.
# Stratejiyi sondan bir önceki mum üzerinden kurmak daha sağlıklıdır.
last_candle = df.iloc[-2]

# Sinyal Mantığı
current_signal = "BEKLE"  # Varsayılan durum

if last_candle['close'] > last_candle['sma']:
    current_signal = "AL"
elif last_candle['close'] < last_candle['sma']:
    current_signal = "SAT"

print(f"Son Kapanış Fiyatı: {last_candle['close']}")
# .5f ile ondalık basamak sayısını sınırladık
print(f"Son SMA Değeri: {last_candle['sma']:.5f}")
print(f"Üretilen Sinyal: {current_signal}")

mt5.shutdown()
