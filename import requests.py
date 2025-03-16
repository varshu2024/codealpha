import requests

# Replace with your Alpha Vantage API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

# Portfolio to store stocks
portfolio = {}

def get_stock_price(symbol):
    """Fetch the current stock price using Alpha Vantage API."""
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if "Global Quote" in data:
        return float(data["Global Quote"]["05. price"])
    else:
        print(f"Error fetching data for {symbol}: {data.get('Note', 'Unknown error')}")
        return None

def add_stock():
    """Add a stock to the portfolio."""
    symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
    shares = int(input("Enter the number of shares: "))
    purchase_price = float(input("Enter the purchase price per share: "))

    if symbol in portfolio:
        print(f"{symbol} is already in your portfolio. Updating shares and purchase price.")
    portfolio[symbol] = {"shares": shares, "purchase_price": purchase_price}
    print(f"{symbol} added to your portfolio.")

def remove_stock():
    """Remove a stock from the portfolio."""
    symbol = input("Enter the stock symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from your portfolio.")
    else:
        print(f"{symbol} not found in your portfolio.")

def view_portfolio():
    """Display the current portfolio with real-time prices and performance."""
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_value = 0
    total_profit_loss = 0

    print("\nStock Portfolio:")
    print("-" * 50)
    print(f"{'Symbol':<10} {'Shares':<10} {'Purchase Price':<15} {'Current Price':<15} {'Value':<15} {'Profit/Loss':<15}")
    print("-" * 50)

    for symbol, data in portfolio.items():
        shares = data["shares"]
        purchase_price = data["purchase_price"]
        current_price = get_stock_price(symbol)

        if current_price is None:
            continue

        value = shares * current_price
        profit_loss = (current_price - purchase_price) * shares

        total_value += value
        total_profit_loss += profit_loss

        print(f"{symbol:<10} {shares:<10} ${purchase_price:<14.2f} ${current_price:<14.2f} ${value:<14.2f} ${profit_loss:<14.2f}")

    print("-" * 50)
    print(f"Total Portfolio Value: ${total_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
    print("-" * 50)

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()