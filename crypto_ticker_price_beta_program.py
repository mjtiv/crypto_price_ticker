#!/usr/bin/env python3.6

import time
import os
from tkinter import *
import sys

# Source Code for Setup from Coin Gecko
# https://www.coingecko.com/learn/python-query-coingecko-api
#
# Notes Program Requires a few packages installed using PIP ###
# pip install requests
# pip install pycoingecko


def clear_screen():
    os.system('cls')

def main():

    # List of Coins of Interest
    list_coins = ['bitcoin', 'ethereum', 'solana', 'chainlink', 'ripple', 'injective-protocol', 'saga-2']

    # API ID Show Slight Variation Create a Dictionary of IDs
    coin_dict = {'bitcoin':'Bitcoin', 'ethereum': 'Ethereum', 'solana': 'Solana', 'chainlink': 'Chainlink',
                 'ripple': 'XRP', 'injective-protocol': 'Injective', 'saga-2': 'SAGA'}

    ################
    # Forever Loop #
    while True:
        for coin in list_coins:
            # API setup for Coin Gecko
            import requests
            url = 'https://api.coingecko.com/api/v3/simple/price'
            params = {
                'ids': coin,
                'vs_currencies': 'USD'
                }

            # Get the Coin Name
            coin_name = coin_dict[coin]

            # Replace 'YOUR_API_KEY' with your actual API key
            headers = { 'x-cg-demo-api-key': 'YOUR_API_KEY' }
            response = requests.get(url, params = params) 
            
            if response.status_code == 200:
                data = response.json()
                coin_price = data[coin]['usd']
                print(f'Price ' + coin_name + ' USD = $' + str(coin_price))
            else:
                print('Failed to retrieve data from the API')
            time.sleep(12)
            clear_screen()

if __name__ == "__main__":
    
    main()
