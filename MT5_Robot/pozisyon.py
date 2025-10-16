import MetaTrader5 as mt5


if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

symbol = "EURUSD"
magic_number = 123456


def acik_pozisyon_var_mi(symbol, magic):
    positions = mt5.positions_get(symbol=symbol)
    if positions:
        for pos in positions:
            if pos.magic == magic:
                return True  # Bizim robotumuza ait açık pozisyon var
    return False


# Test
if acik_pozisyon_var_mi(symbol, magic_number):
    print(f"{symbol} paritesinde robotumuza ait açık bir pozisyon var.")
else:
    print(f"{symbol} paritesinde robotumuza ait açık bir pozisyon YOK.")

mt5.shutdown()
