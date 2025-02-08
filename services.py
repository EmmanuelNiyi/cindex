import requests

"""SERVICES LAYER"""


def get_top_10_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 15,
        'page': 1,
        'sparkline': False
    }
    response = requests.get(url, params=params)
    cryptos = response.json()

    # Extract the required information for each cryptocurrency
    crypto_data = []
    excluded = ['usdt', "usdc", "steth", "wbtc", "wsteth"]
    for currency in cryptos:
        if currency['symbol'] not in excluded:
            crypto_info = {
                'id': currency['id'],
                'name': currency['name'],
                'price': currency['current_price'],
                'symbol': currency['symbol'].upper(),
                'image': currency['image']
            }
            crypto_data.append(crypto_info)

    return crypto_data


def calculate_investment_amount(deposit_amount, num_cryptos=10):
    amount_to_be_invested = deposit_amount / num_cryptos
    print(f"Amount to be invested: {amount_to_be_invested}")
    return amount_to_be_invested


def invest_in_top_10_currencies(client, amount_to_be_invested):
    top_10_coins = get_top_10_cryptos()

    for currency in top_10_coins:
        currency_symbol = f"{currency['symbol']}"
        print(currency_symbol)

        currency_balance = client.get_asset_balance(asset=currency_symbol)
        print(currency_balance)

        # Place order
        currency_pair = currency_symbol + "USDT"
        invest_in_crypto(client, currency_pair, amount_to_be_invested)

        currency_balance = client.get_asset_balance(asset=currency_symbol)
        print(currency_balance)


def print_wallet_balance_of_top10_cryptos(client):
    top_10_coins = get_top_10_cryptos()

    for currency in top_10_coins:
        currency_symbol = f"{currency['symbol']}"
        currency_balance = client.get_asset_balance(asset=currency_symbol)
        print(currency_balance)


def invest_in_crypto(client, symbol, amount):
    try:
        order = client.order_market_buy(
            symbol=symbol,
            quoteOrderQty=amount  # Amount in USDT
        )
        # print(f"Order executed: {order}")
        print(f"amount purchased: {order['executedQty']}")
    except Exception as e:
        print(f"Error executing order: {e}")
