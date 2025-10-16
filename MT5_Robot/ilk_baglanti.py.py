# Gerekli kütüphaneyi içe aktarır
import MetaTrader5 as mt5

# MetaTrader 5 terminaline bağlanmayı başlatır
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()  # Bağlantı başarısızsa programı sonlandır

# Bağlantı başarılıysa devam eder
print("MetaTrader 5'e başarıyla bağlandı!")

# Bağlı olduğumuz hesap hakkındaki bilgileri al
account_info = mt5.account_info()
if account_info != None:
    # Bilgileri ekrana yazdırır
    print("Hesap Sahibi:", account_info.name)
    print("Hesap Numarası:", account_info.login)
    print("Bakiye:", account_info.balance, account_info.currency)
else:
    print("Hesap bilgileri alınamadı, hata kodu =", mt5.last_error())

# MetaTrader 5 ile bağlantıyı sonlandır
mt5.shutdown()
