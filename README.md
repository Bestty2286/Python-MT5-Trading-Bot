# Simple SMA Crossover Trading Bot for MetaTrader 5

A simple algorithmic trading bot using Python and the MetaTrader 5 API based on a Simple Moving Average (SMA) crossover strategy. This project was developed to apply computer science principles to real-world financial markets.

---

### 🚀 Key Features

- **Connects** directly to the MetaTrader 5 terminal.
- **Fetches** real-time and historical market data for any symbol.
- **Calculates** technical indicators like Simple Moving Average (SMA) using Pandas.
- **Executes** BUY and SELL market orders automatically based on the strategy logic.
- **Checks** for existing open positions to avoid duplicate trades.

### 🛠️ Technologies Used

- **Language:** Python
- **Libraries:** MetaTrader5, Pandas
- **Platform:** MetaTrader 5

---

### 📈 Strategy Explained

The core logic of this bot is based on a **20-period Simple Moving Average (SMA)** crossover strategy on a 1-minute timeframe.

- **BUY Signal:** A buy order is triggered when the closing price of the previous candle moves *above* the SMA line.
- **SELL Signal:** A sell order is triggered when the closing price of the previous candle moves *below* the SMA line.
- The bot only looks for a new signal if there are no other open positions with its specific "Magic Number".

### ⚙️ Setup and Usage

1.  Ensure you have Python and MetaTrader 5 installed.
2.  Install the required libraries:
    ```sh
    pip install MetaTrader5 pandas
    ```
3.  In the MetaTrader 5 terminal, go to `Tools -> Options -> Expert Advisors` and check "Allow algorithmic trading".
4.  Run the `expert.py` script.

### Future Improvements

- [ ] Implementing a robust backtesting module.
- [ ] Adding risk management features (Stop-Loss and Take-Profit).
- [ ] Integrating other technical indicators (e.g., RSI, MACD) for more complex strategies.
- [ ] Developing a more sophisticated logging system.

### ⚠️ Disclaimer

This project is for educational purposes only. It is not financial advice. Trading in financial markets involves substantial risk.
