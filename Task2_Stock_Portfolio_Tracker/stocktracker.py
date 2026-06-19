# ============================================================
#  CodeAlpha Internship — Task 2: Stock Portfolio Tracker
#  NSE/BSE Indian stocks — prices in Indian Rupees (₹)
#  Saves results to both .txt and .csv files
# ============================================================

import csv
import os
from datetime import datetime

# ── Hardcoded NSE/BSE stock prices (price in INR ₹) ─────────
STOCK_PRICES = {
    "RELIANCE":  2925.00,   # Reliance Industries
    "TCS":       3850.00,   # Tata Consultancy Services
    "INFY":      1445.00,   # Infosys
    "HDFCBANK":  1620.00,   # HDFC Bank
    "WIPRO":      480.00,   # Wipro
    "SBIN":       810.00,   # State Bank of India
    "TATAMOTORS": 975.00,   # Tata Motors
    "ONGC":       265.00,   # Oil & Natural Gas Corp
    "BAJFINANCE": 6900.00,  # Bajaj Finance
    "ICICIBANK":  1280.00,  # ICICI Bank
}


def show_available_stocks():
    """Display all available NSE stocks and their prices."""
    print("\n📈 Available NSE/BSE Stocks:")
    print(f"  {'Symbol':<12} {'Company':<30} {'Price (₹)':>10}")
    print("  " + "-" * 56)
    names = {
        "RELIANCE": "Reliance Industries",
        "TCS": "Tata Consultancy Services",
        "INFY": "Infosys",
        "HDFCBANK": "HDFC Bank",
        "WIPRO": "Wipro",
        "SBIN": "State Bank of India",
        "TATAMOTORS": "Tata Motors",
        "ONGC": "Oil & Natural Gas Corp",
        "BAJFINANCE": "Bajaj Finance",
        "ICICIBANK": "ICICI Bank",
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<12} {names[symbol]:<30} ₹{price:>9.2f}")


def get_portfolio():
    """Prompt user to enter stock symbols and quantities."""
    portfolio = {}
    print("\nEnter your stock holdings. Type 'done' when finished.")
    print("(Symbols are case-insensitive, e.g. tcs or TCS)\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            break

        if not symbol:
            continue

        if symbol not in STOCK_PRICES:
            print(f"  ⚠️  '{symbol}' not found. Available: {', '.join(STOCK_PRICES)}\n")
            continue

        try:
            qty = int(input(f"  How many shares of {symbol}? "))
            if qty <= 0:
                print("  ⚠️  Please enter a positive number.\n")
                continue
        except ValueError:
            print("  ⚠️  Invalid number, try again.\n")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"  ✅ Updated {symbol} to {portfolio[symbol]} shares.\n")
        else:
            portfolio[symbol] = qty
            print(f"  ✅ Added {qty} share(s) of {symbol}.\n")

    return portfolio


def format_inr(amount):
    """Format a number in Indian numbering system (lakhs, crores)."""
    # Convert to int string for Indian grouping
    s = f"{amount:.2f}"
    integer_part, decimal_part = s.split(".")
    n = len(integer_part)
    if n <= 3:
        return f"₹{integer_part}.{decimal_part}"
    # First group of 3, then groups of 2
    result = integer_part[-3:]
    integer_part = integer_part[:-3]
    while integer_part:
        result = integer_part[-2:] + "," + result
        integer_part = integer_part[:-2]
    return f"₹{result}.{decimal_part}"


def calculate_summary(portfolio):
    """Return rows with investment details and the grand total."""
    rows = []
    total = 0.0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        rows.append({
            "Symbol": symbol,
            "Price (INR)": price,
            "Quantity": qty,
            "Value (INR)": value,
        })

    return rows, total


def display_summary(rows, total):
    """Print a formatted portfolio summary to the console."""
    print("\n" + "=" * 58)
    print("         📊 NSE/BSE PORTFOLIO SUMMARY")
    print("=" * 58)
    print(f"  {'Symbol':<12} {'Price (₹)':>12}  {'Qty':>5}  {'Value (₹)':>14}")
    print("  " + "-" * 50)
    for r in rows:
        print(f"  {r['Symbol']:<12} {format_inr(r['Price (INR)']):>12}  "
              f"{r['Quantity']:>5}  {format_inr(r['Value (INR)']):>14}")
    print("  " + "-" * 50)
    print(f"  {'TOTAL':>31}  {format_inr(total):>14}")
    print("=" * 58)

    # Show in lakhs/crores for easy reading
    if total >= 1_00_00_000:
        print(f"\n  💰 Total Investment: ₹{total/1_00_00_000:.2f} Crore")
    elif total >= 1_00_000:
        print(f"\n  💰 Total Investment: ₹{total/1_00_000:.2f} Lakh")
    else:
        print(f"\n  💰 Total Investment: {format_inr(total)}")


def save_to_txt(rows, total, filename="portfolio_report.txt"):
    """Save the portfolio summary to a .txt file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("CodeAlpha NSE/BSE Stock Portfolio Tracker\n")
        f.write(f"Generated: {timestamp}\n")
        f.write("=" * 58 + "\n")
        f.write(f"{'Symbol':<12} {'Price (INR)':>14}  {'Qty':>5}  {'Value (INR)':>14}\n")
        f.write("-" * 52 + "\n")
        for r in rows:
            f.write(f"{r['Symbol']:<12} {format_inr(r['Price (INR)']):>14}  "
                    f"{r['Quantity']:>5}  {format_inr(r['Value (INR)']):>14}\n")
        f.write("-" * 52 + "\n")
        f.write(f"{'TOTAL':>35}  {format_inr(total):>14}\n")
    print(f"\n  💾 Saved to: {os.path.abspath(filename)}")


def save_to_csv(rows, total, filename="portfolio_report.csv"):
    """Save the portfolio summary to a .csv file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Symbol", "Price (INR)", "Quantity", "Value (INR)"])
        writer.writeheader()
        writer.writerows(rows)
        writer.writerow({"Symbol": "TOTAL", "Price (INR)": "", "Quantity": "", "Value (INR)": total})
    print(f"  📊 Saved to: {os.path.abspath(filename)}")


def main():
    print("=" * 58)
    print("   📈 CodeAlpha NSE/BSE Stock Portfolio Tracker")
    print("=" * 58)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\n⚠️  No stocks entered. Exiting.")
        return

    rows, total = calculate_summary(portfolio)
    display_summary(rows, total)

    save_choice = input("\nSave report? (txt / csv / both / no): ").strip().lower()
    if save_choice in ["txt", "both"]:
        save_to_txt(rows, total)
    if save_choice in ["csv", "both"]:
        save_to_csv(rows, total)

    print("\n✅ Done! Thank you for using the NSE/BSE Portfolio Tracker.")


if __name__ == "__main__":
    main()
