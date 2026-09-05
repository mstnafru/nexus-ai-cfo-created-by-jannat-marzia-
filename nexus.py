import urllib.request
import json

# ==============================
# NEXUS — AUTONOMOUS CRYPTO CFO
# ==============================

PORTFOLIO = {
    "BTCUSDT": 0.05,
    "ETHUSDT": 1.2,
    "BNBUSDT": 15.0
}

MAX_CONCENTRATION = 0.40


def get_price(symbol):
    url = (
        "https://api.binance.com/api/v3/ticker/price"
        f"?symbol={symbol}"
    )

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read())
            return float(data["price"])
    except Exception:
        return None


def analyze():
    print()
    print("=" * 55)
    print("        NEXUS — AUTONOMOUS CRYPTO CFO")
    print("=" * 55)
    print()

    prices = {}

    for symbol in PORTFOLIO:
        price = get_price(symbol)

        if price is None:
            print(f"Could not get price for {symbol}")
            return

        prices[symbol] = price

    # Calculate portfolio values
    values = {}

    for symbol, amount in PORTFOLIO.items():
        values[symbol] = prices[symbol] * amount

    total = sum(values.values())

    print(f"Portfolio Value: ${total:,.2f}")
    print()
    print("-" * 55)

    # Show portfolio
    for symbol in PORTFOLIO:
        weight = values[symbol] / total

        print(
            f"{symbol:10} "
            f"${prices[symbol]:>12,.2f}   "
            f"Weight: {weight:>6.1%}"
        )

    print("-" * 55)
    print()

    # Find biggest concentration
    biggest_symbol = max(values, key=values.get)
    biggest_weight = values[biggest_symbol] / total

    print("NEXUS CFO ANALYSIS")
    print()

    if biggest_weight >= MAX_CONCENTRATION:

        print("🔴 HIGH PRIORITY RISK")
        print()
        print(
            f"{biggest_symbol} represents "
            f"{biggest_weight:.1%} of your portfolio."
        )

        print(
            f"The configured concentration limit is "
            f"{MAX_CONCENTRATION:.0%}."
        )

        print()
        print("WHY THIS MATTERS:")
        print(
            "A large allocation to one asset means "
            "your portfolio is highly exposed to "
            "that asset's price movement."
        )

        print()
        print("NEXUS RECOMMENDATION:")
        print(
            f"Consider reducing {biggest_symbol} exposure "
            f"toward the configured risk limit."
        )

        print()
        print("WORKFLOW ACTION:")
        print("CREATE_REBALANCE_PLAN")

    else:

        print("🟢 PORTFOLIO WITHIN LIMITS")
        print()
        print(
            "No concentration risk exceeded "
            "the configured threshold."
        )

        print()
        print("NEXUS RECOMMENDATION:")
        print("Continue monitoring the portfolio.")

    print()
    print("=" * 55)
    print("NEXUS: DATA → ANALYSIS → DECISION")
    print("=" * 55)
    print()


if __name__ == "__main__":
    analyze()
