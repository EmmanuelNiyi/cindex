import os
from decimal import Decimal

from dotenv import load_dotenv
from ground import get_top_10_cryptos
from binance.client import Client

from services import calculate_investment_amount, invest_in_top_10_currencies, print_wallet_balance_of_top10_cryptos

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key and secret from the environment
binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_SECRET")

# Print the values
print(f"Binance API Key: {binance_api_key}")
print(f"Binance API Secret: {binance_api_secret}")

client = Client(binance_api_key, binance_api_secret)

print(client.get_asset_balance(asset="USDT"))

usdt_balance = Decimal(client.get_asset_balance(asset="USDT")["free"])

if usdt_balance > 50:
    print(f"USDT balance: {usdt_balance}. Adequate")
else:
    print(f"USDT balance: {usdt_balance}. Insufficient funds")

top_10_coins = get_top_10_cryptos()

amount_to_be_invested = calculate_investment_amount(usdt_balance)

invest_in_top_10_currencies(client, amount_to_be_invested=amount_to_be_invested)

print_wallet_balance_of_top10_cryptos(client)
