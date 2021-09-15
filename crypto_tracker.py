import requests


def get_prices():
    coins = ["BTC", "ETH", "ADA", "LINK"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for coin in crypto_data:
        data[coin] = {
            "coin": coin,
            "price": crypto_data[coin]["USD"]["PRICE"],
            "change_day": crypto_data[coin]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[coin]["USD"]["CHANGEPCTHOUR"]
        }
    return data


if __name__ == "__main__":
    print(get_prices())
