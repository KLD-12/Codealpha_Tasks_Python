import csv
from datetime import datetime


STOCK_PRICES = {
    "RELIANCE": 2950,
    "TCS": 3850,
    "INFY": 1650,
    "HDFCBANK": 1620,
    "ICICIBANK": 1145,
    "SBIN": 825,
    "TATAMOTORS": 980,
    "WIPRO": 565,
    "ITC": 465,
    "BAJFINANCE": 7150,
}


def show_available_stocks():
    print("\nAvailable stocks (NSE) and current price (₹):")
    print("-" * 40)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<12} ₹{price:,.2f}")
    print("-" * 40)


def get_user_portfolio():
    portfolio = {}

    print("\nEnter stock symbol and quantity (type 'done' as the symbol to finish).")

    while True:
        symbol = input("\nStock symbol: ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' not found in the price list. Try again "
                  f"or type 'list' to see available stocks.")
            if symbol == "LIST":
                show_available_stocks()
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()

         

        price = STOCK_PRICES[symbol]
        value = price * quantity

        if symbol in portfolio:
            portfolio[symbol]["quantity"] += quantity
            portfolio[symbol]["value"] = portfolio[symbol]["quantity"] * price
        else:
            portfolio[symbol] = {
                "quantity": quantity,
                "price": price,
                "value": value,
            }

        print(f"Added: {quantity} share(s) of {symbol} @ ₹{price:,.2f} = ₹{value:,.2f}")

    return portfolio


def display_summary(portfolio):
    if not portfolio:
        print("\nNo stocks were added. Nothing to summarize.")
        return 0

    print("\n" + "=" * 55)
    print(f"{'PORTFOLIO SUMMARY':^55}")
    print("=" * 55)
    print(f"{'Stock':<12}{'Qty':>8}{'Price (₹)':>15}{'Value (₹)':>18}")
    print("-" * 55)

    total = 0
    for symbol, data in portfolio.items():
        print(f"{symbol:<12}{data['quantity']:>8}{data['price']:>15,.2f}{data['value']:>18,.2f}")
        total += data["value"]

    print("-" * 55)
    print(f"{'TOTAL INVESTMENT':<35}{'₹' + format(total, ',.2f'):>20}")
    print("=" * 55)

    return total


def save_to_file(portfolio, total, file_format="txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if file_format == "csv":
        filename = f"portfolio_summary_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price (INR)", "Value (INR)"])
            for symbol, data in portfolio.items():
                writer.writerow([symbol, data["quantity"], data["price"], data["value"]])
            writer.writerow([])
            writer.writerow(["TOTAL INVESTMENT", "", "", total])
    else:
        filename = f"portfolio_summary_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write(f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            f.write("=" * 55 + "\n")
            f.write(f"{'Stock':<12}{'Qty':>8}{'Price (Rs)':>15}{'Value (Rs)':>18}\n")
            f.write("-" * 55 + "\n")
            for symbol, data in portfolio.items():
                f.write(f"{symbol:<12}{data['quantity']:>8}{data['price']:>15,.2f}{data['value']:>18,.2f}\n")
            f.write("-" * 55 + "\n")
            f.write(f"TOTAL INVESTMENT: Rs {total:,.2f}\n")

    print(f"\nSummary saved to '{filename}'")


def main():
    print("=" * 55)
    print(f"{'INDIAN STOCK PORTFOLIO TRACKER':^55}")
    print("=" * 55)

    show_available_stocks()

    portfolio = get_user_portfolio()
    total = display_summary(portfolio)

    if portfolio:
        choice = input("\nSave summary to a file? (y/n): ").strip().lower()
        if choice == "y":
            fmt = input("Choose format - txt or csv: ").strip().lower()
            fmt = fmt if fmt in ("txt", "csv") else "txt"
            save_to_file(portfolio, total, fmt)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
