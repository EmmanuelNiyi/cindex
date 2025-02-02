import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key and secret from the environment
binance_testnet_api_key = os.getenv("BINANCE_API_KEY_TEST")
binance_testnet_api_secret = os.getenv("BINANCE_API_SECRET_TEST")

# Print the values
print(f"Binance Testnet API Key: {binance_testnet_api_key}")
print(f"Binance Testnet API Secret: {binance_testnet_api_secret}")


from binance.client import Client

client = Client(binance_testnet_api_key, binance_testnet_api_secret)

client.API_URL = 'https://testnet.binance.vision/api'
# get balances for all assets & some account information
# print(client.get_account())

print(client.get_asset_balance(asset='BTC'))
print(client.get_asset_balance(asset='ETH'))
print(client.get_asset_balance(asset='ADA'))
print(client.get_asset_balance(asset='LINK'))
print(client.get_asset_balance(asset='BNB'))
print(client.get_asset_balance(asset='XRP'))
print(client.get_asset_balance(asset='DOGE'))
print(client.get_asset_balance(asset='LTC'))
print(client.get_asset_balance(asset='USDT'))


# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
# print full output (dictionary)
print(btc_price)
# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol="ADAUSDT")
# print full output (dictionary)
print(btc_price)


