# CodeAlpha Python Programming Internship - Task 2
# Project: Stock Portfolio Tracker
# Description: A console-based stock portfolio tracker that allows users to manage their stock portfolio, 
#              calculate investment values based on a predefined set of stock prices, and optionally 
#              save their portfolio summary to a text file.

import os

# Step 1: Predefined stock database with current stock prices (minimum of 5 stocks)
STOCK_PRICES = {
    "AAPL": 175.50,   # Apple Inc.
    "TSLA": 220.00,   # Tesla Inc.
    "GOOGL": 140.25,  # Alphabet Inc.
    "MSFT": 380.75,  # Microsoft Corp.
    "AMZN": 145.10   # Amazon.com Inc.
}


def display_market_prices():
    """Displays the available stocks and their current market prices."""
    print("\n" + "=" * 45)
    print("      AVAILABLE STOCKS & MARKET PRICES")
    print("=" * 45)
    print(f" {'Symbol':<10} | {'Stock Name':<20} | {'Price ($)':<10}")
    print("-" * 45)
    
    # Mapping symbols to readable names for better user experience
    names = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet Inc.",
        "MSFT": "Microsoft Corp.",
        "AMZN": "Amazon.com Inc."
    }
    
    for symbol, price in STOCK_PRICES.items():
        name = names.get(symbol, "Unknown Stock")
        print(f" {symbol:<10} | {name:<20} | ${price:<10.2f}")
    print("=" * 45 + "\n")


def get_positive_integer(prompt):
    """Prompts the user for a positive integer and validates it."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val <= 0:
                print("Error: Please enter a number greater than 0.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")


def get_positive_float(prompt):
    """Prompts the user for a positive floating-point number and validates it."""
    while True:
        try:
            val = float(input(prompt).strip())
            if val <= 0:
                print("Error: Quantity must be greater than 0.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a valid number (e.g., 10 or 12.5).")


def get_valid_stock_symbol(prompt):
    """Prompts the user for a stock symbol and ensures it exists in the market database."""
    while True:
        symbol = input(prompt).strip().upper()
        if symbol in STOCK_PRICES:
            return symbol
        else:
            print(f"Error: '{symbol}' is not a recognized stock symbol.")
            print("Available symbols: " + ", ".join(STOCK_PRICES.keys()))


def generate_portfolio_summary_string(portfolio):
    """Generates a formatted string representing the portfolio summary."""
    lines = []
    lines.append("=" * 65)
    lines.append("                      STOCK PORTFOLIO SUMMARY")
    lines.append("=" * 65)
    lines.append(f" {'Symbol':<10} | {'Price ($)':<12} | {'Quantity':<12} | {'Value ($)':<15}")
    lines.append("-" * 65)
    
    total_portfolio_value = 0.0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        investment_value = price * quantity
        total_portfolio_value += investment_value
        lines.append(f" {symbol:<10} | ${price:<11.2f} | {quantity:<12.4f} | ${investment_value:<14.2f}")
        
    lines.append("-" * 65)
    lines.append(f" {'TOTAL PORTFOLIO VALUE:':<39} | ${total_portfolio_value:<14.2f}")
    lines.append("=" * 65)
    return "\n".join(lines), total_portfolio_value


def main():
    print("+" * 50)
    print("Welcome to the CodeAlpha Stock Portfolio Tracker!")
    print("+" * 50)
    
    # Show available stocks
    display_market_prices()
    
    # Step 2: Ask user for the number of different stocks they own
    num_stocks = get_positive_integer("How many different stocks do you own in your portfolio? ")
    
    # Dictionary to store the user's portfolio: { symbol: quantity }
    portfolio = {}
    
    # Step 3: Accept stock symbols and quantities from the user
    for i in range(1, num_stocks + 1):
        print(f"\nEntering details for Stock #{i}:")
        symbol = get_valid_stock_symbol(f"  Enter stock symbol (e.g., AAPL): ")
        
        # Check if the user has already entered this symbol
        if symbol in portfolio:
            print(f"  Note: You already have {portfolio[symbol]} shares of {symbol} in your tracker.")
            print("  1. Add to existing quantity")
            print("  2. Replace existing quantity")
            choice = input("  Select option (1 or 2): ").strip()
            
            quantity = get_positive_float(f"  Enter quantity: ")
            if choice == '1':
                portfolio[symbol] += quantity
                print(f"  Updated: New total quantity of {symbol} is {portfolio[symbol]} shares.")
            else:
                portfolio[symbol] = quantity
                print(f"  Updated: {symbol} quantity replaced with {portfolio[symbol]} shares.")
        else:
            quantity = get_positive_float(f"  Enter quantity of {symbol} shares: ")
            portfolio[symbol] = quantity

    # Step 4 & 5: Calculate and display investment values & total portfolio value
    summary_table, total_value = generate_portfolio_summary_string(portfolio)
    
    print("\nCalculations complete! Here is your portfolio summary:\n")
    print(summary_table)
    
    # Step 7: Optionally save the portfolio summary to a .txt file
    save_choice = input("\nWould you like to save this summary to a text file? (y/n): ").strip().lower()
    if save_choice in ['y', 'yes']:
        filename = "portfolio_summary.txt"
        try:
            with open(filename, "w") as file:
                file.write("CodeAlpha Stock Portfolio Tracker Summary\n")
                file.write(summary_table)
                file.write("\n\nGenerated on behalf of Naveena C B.\n")
            print(f"\n[Success] Portfolio summary successfully saved to '{os.path.abspath(filename)}'")
        except Exception as e:
            print(f"\n[Error] Could not save file: {e}")
            
    print("\nThank you for using the Stock Portfolio Tracker! Keep investing!")


if __name__ == "__main__":
    main()
