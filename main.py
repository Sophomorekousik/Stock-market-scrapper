import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)
    data = stock.history(start=start_date, end=end_date)
    if data.empty:
        print(f"No data found for {stock_symbol} between {start_date} and {end_date}.")
        return None
    return data

def visualize_stock_data(data):
    if data is None or data.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-')
    plt.title('Stock Price Movement')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple Inc.): ")
    num_days = int(input("Enter the number of days of data to fetch: "))

    end_date = pd.Timestamp.today()
    start_date = end_date - pd.Timedelta(days=num_days)

    data = fetch_stock_data(stock_symbol, start_date, end_date)

    if data is not None:
        # print("Stock Data:")
        # print(data[['Close']])
        visualize_stock_data(data)

if __name__ == "__main__":
    main()
