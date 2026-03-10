def stock_tracker():
    # Hardcoded prices as per the task requirements
    prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150, "MSFT": 400}
    portfolio = {}
    
    print("--- Stock Portfolio Tracker ---")
    
    # User Input
    while True:
        symbol = input("Enter Stock Symbol (or type 'done'): ").upper()
        if symbol == 'DONE': break
        
        if symbol in prices:
            qty = int(input(f"Enter quantity for {symbol}: "))
            portfolio[symbol] = qty
        else:
            print("Stock not found in our list.")

    # Calculate Total
    total_value = 0
    report = "Stock Portfolio Report:\n"
    for stock, qty in portfolio.items():
        value = qty * prices[stock]
        total_value += value
        report += f"{stock}: {qty} shares | Value: ${value}\n"
    
    report += f"Total Portfolio Value: ${total_value}"
    
    # Save to file
    with open("portfolio.txt", "w") as file:
        file.write(report)
    
    print("\n" + report)
    print("\nReport saved to portfolio.txt")

stock_tracker()

