import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key and secret from the environment
binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_SECRET")

# Print the values
print(f"Binance API Key: {binance_api_key}")
print(f"Binance API Secret: {binance_api_secret}")


from binance.client import Client

client = Client(binance_api_key, binance_api_secret)
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
