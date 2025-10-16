import MetaTrader5 as mt5

# ... (Bağlantı kodu buraya gelecek) ...
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

symbol = "EURUSD"
lot = 0.01  # İşlem hacmi


def satis_emri_gonder(symbol, lot):
    print(f"{symbol} için Satış Emri gönderiliyor...")

    # Sembol için anlık satış fiyatını al
    point = mt5.symbol_info(symbol).point
    ask_price = mt5.symbol_info_tick(symbol).ask

    # Emir isteği sözlüğünü hazırla
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
        "deviation": 20,  # Fiyattaki maksimum sapma (pip)
        "magic": 123456,  # Robotun kendi emirlerini tanıması için sihirli numara
        "comment": "Python Satis Emri",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    # Emri gönder
    result = mt5.order_send(request)

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Emir gönderilemedi, retcode={result.retcode}")
        # Hata detaylarını yazdır
        print(result)
    else:
        print(f"Emir başarıyla gönderildi! Pozisyon #{result.order}")


# Örnek: Satış emri göndermeyi test et
satis_emri_gonder(symbol, lot)

mt5.shutdown()
