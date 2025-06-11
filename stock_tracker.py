# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 310,
    "AMZN": 3400
}

# Ask user for input
total_investment = 0
user_stocks = {}

print("Enter the stock name and quantity (type 'done' to finish):")
while True:
    stock = input("Stock Symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in list! Try AAPL, TSLA, GOOGL, MSFT, AMZN")
        continue
    try:
        qty = int(input("Quantity: "))
        user_stocks[stock] = qty
    except ValueError:
        print("Enter a valid number.")

# Calculate total
print("\nYour Investment Summary:")
for stock, qty in user_stocks.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock}: {qty} x ${price} = ${value}")
    total_investment += value

print("\nTotal Investment Value: $", total_investment)
