import sys
import requests


def main():
    try:
        if len(sys.argv) == 2:
            amount = float(sys.argv[1])
            usd_price = get_bitcoin_price()
            total_usd = amount * usd_price
            print(f"${total_usd:,.4f}")
        else:
            sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price():
    try:
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        usd = res["bpi"]["USD"]["rate_float"]
        return usd
    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()
