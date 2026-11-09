
# STOCK PORTFOLIO TRACKER

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 170
}

# Empty portfolio
portfolio = {}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

# Display available stocks
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Add multiple stocks
while True:
    stock = input(
        "\nEnter stock symbol to add (or 'done' to finish): "
    ).strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock symbol! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"{quantity} shares of {stock} added successfully!")

    except ValueError:
        print("Invalid quantity! Enter a whole number.")

# Display portfolio summary
print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")

total_value = 0

if not portfolio:
    print("No stocks added to portfolio.")

else:
    print("\nStock   Quantity   Price   Total")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        total_value += value

        print(f"{stock:<8} {quantity:<10} ${price:<7} ${value}")

    print("--------------------------------")
    print(f"Total Portfolio Value: ${total_value}")

print("\nThank you for using Stock Portfolio Tracker!")
