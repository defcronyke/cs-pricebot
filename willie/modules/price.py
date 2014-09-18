# TODO: Check if coin is on coin-swap.
# If more than one market, output prices for all markets.

import willie
import urllib.request
import json

@willie.module.commands('price')
def price(bot, trigger):
    """ Get price and info of coins on coin-swap.net. Usage: !price coin_symbol """
    command = trigger.group(1)
    coin = trigger.group(2)
    if not coin:
        bot.say("Usage: !%s coin_symbol" % command)
        return
    
    primary_currencies = ["BTC", "DOGE"]
    
    for primary_currency in primary_currencies:
        req = "https://api.coin-swap.net/market/stats/%s/%s" % (coin, primary_currency)
        res = urllib.request.urlopen(req)
        str_res = res.readall().decode('utf-8')
        
        if str_res != "{}":
            print("JSON Response: %s\n" % str_res)
            dict_res = json.loads(str_res)
            bot_response = "coin-swap.net market: %s/%s | last price: %s %s | 24hr volume: %s %s | 24hr high: %s %s | 24hr low: %s %s | sell price: %s %s | buy price: %s %s" % (
                 coin.upper(), 
                 primary_currency.upper(), 
                 dict_res["lastprice"], 
                 primary_currency,
                 dict_res["dayvolume"],
                 primary_currency,
                 dict_res["dayhigh"],
                 primary_currency,
                 dict_res["daylow"],
                 primary_currency,
                 dict_res["ask"],
                 primary_currency,
                 dict_res["bid"],
                 primary_currency)
    
            bot.say("%s" % bot_response)