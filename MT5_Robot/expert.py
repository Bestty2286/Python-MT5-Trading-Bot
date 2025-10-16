import MetaTrader5 as mt5
import pandas as pd
import time

# --- AYARLAR ---
SYMBOL = "EURUSD"
TIMEFRAME = mt5.TIMEFRAME_M1  # 1 Dakikalık periyot
VOLUME = 0.01
MAGIC_NUMBER = 123456
SMA_PERIOD = 20

# --- MT5 BAĞLANTISI ---
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

print("Robot Başlatıldı...")

# --- ANA DÖNGÜ ---
try:
    while True:
        # Mevcut açık pozisyon var mı kontrol et
        positions = mt5.positions_get(symbol=SYMBOL)
        position_open = False
        if positions:
            for pos in positions:
                if pos.magic == MAGIC_NUMBER:
                    position_open = True
                    break

        # Veri çek ve SMA hesapla
        rates = mt5.copy_rates_from_pos(SYMBOL, TIMEFRAME, 0, 100)
        df = pd.DataFrame(rates)
        df['sma'] = df['close'].rolling(window=SMA_PERIOD).mean()

        last_candle = df.iloc[-2]

        # --- STRATEJİ VE EMİR GÖNDERME ---
        if not position_open:  # Eğer açık pozisyon yoksa sinyal ara
            print(
                f"Açık pozisyon yok, sinyal kontrol ediliyor. Son Fiyat: {last_candle['close']}, SMA: {last_candle['sma']:.5f}")

            # AL SİNYALİ
            if last_candle['close'] > last_candle['sma']:
                print("AL SİNYALİ TESPİT EDİLDİ! Emir gönderiliyor...")
                tick = mt5.symbol_info_tick(SYMBOL)
                request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": SYMBOL, "volume": VOLUME, "type": mt5.ORDER_TYPE_BUY,
                    "price": tick.ask, "deviation": 20, "magic": MAGIC_NUMBER,
                    "comment": "Python AL", "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_FOK,
                }
                result = mt5.order_send(request)
                if result.retcode == mt5.TRADE_RETCODE_DONE:
                    print("Alış emri başarıyla gönderildi.")
                else:
                    print(f"Alış emri gönderilemedi, retcode={result.retcode}")

            # SAT SİNYALİ
            elif last_candle['close'] < last_candle['sma']:
                print("SAT SİNYALİ TESPİT EDİLDİ! Emir gönderiliyor...")
                tick = mt5.symbol_info_tick(SYMBOL)
                request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": SYMBOL, "volume": VOLUME, "type": mt5.ORDER_TYPE_SELL,
                    "price": tick.bid, "deviation": 20, "magic": MAGIC_NUMBER,
                    "comment": "Python SAT", "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_FOK,
                }
                result = mt5.order_send(request)
                if result.retcode == mt5.TRADE_RETCODE_DONE:
                    print("Satış emri başarıyla gönderildi.")
                else:
                    print(
                        f"Satış emri gönderilemedi, retcode={result.retcode}")
            else:
                print("Net bir sinyal yok, bekleniyor...")

        else:
            print("Zaten açık bir pozisyon var. Yeni sinyal için bekleniyor.")

        # Döngü arasında bekleme
        print("60 saniye bekleniyor...")
        time.sleep(60)

except KeyboardInterrupt:  # Ctrl+C ile programı durdurmak için
    print("\nRobot durduruldu.")
    mt5.shutdown()
