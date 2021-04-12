# write your code here!

# solution stage 4:
#
# number_of_conicoins = float(input())
# # exchange_rate = float(input())
# RUB = number_of_conicoins * 2.98
# ARS = number_of_conicoins * 0.82
# HNL = number_of_conicoins * 0.17
# AUD = number_of_conicoins * 1.9622
# MAD = number_of_conicoins * 0.208
# print(f"""I will get {RUB:.2f} RUB from the sale of {number_of_conicoins} conicoins.
# I will get {ARS:.2f} ARS from the sale of {number_of_conicoins} conicoins.
# I will get {HNL:.2f} HNL from the sale of {number_of_conicoins} conicoins.
# I will get {AUD:.2f} AUD from the sale of {number_of_conicoins} conicoins.
# I will get {MAD:.2f} MAD from the sale of {number_of_conicoins} conicoins.""")

# stage 5 solution:

# import requests
#
# currency_code = input()
#
#
# def get_currency_rates(request_string):
#     r = requests.get(request_string)
#     exchange_rates = r.json()
#     return exchange_rates['usd'], exchange_rates['eur']
#
#
# usd_rate, eur_rate = get_currency_rates("http://www.floatrates.com/daily/" + currency_code + ".json")
# print(usd_rate, eur_rate, sep='\n')


# solution stage 6:


import requests

exchange_rates_cache = {}


def get_exchange_rates(currency_code):
    request_string = "http://www.floatrates.com/daily/" + currency_code + ".json"
    r = requests.get(request_string)
    exchange_rates = r.json()
    return exchange_rates


from_currency_code = input().lower()
rates = get_exchange_rates(from_currency_code)
if from_currency_code != 'usd':
    exchange_rates_cache['usd'] = rates['usd']['rate']

if from_currency_code != 'eur':
    exchange_rates_cache['eur'] = rates['eur']['rate']

while True:
    to_currency_code = input().lower()
    if to_currency_code == "":
        break
    amount_to_exchange = float(input())

    print("Checking the cache...")
    if to_currency_code in exchange_rates_cache:
        print(
            f"""Oh! It is in the cache!\nYou received {float(exchange_rates_cache[to_currency_code]) * amount_to_exchange:.2f} {to_currency_code.upper()}.""")
    elif from_currency_code not in exchange_rates_cache:
        print("Sorry, but it is not in the cache!")
        exchange_rates_cache[to_currency_code] = get_exchange_rates(from_currency_code)[to_currency_code]['rate']
        print(
            f"You received {float(exchange_rates_cache[to_currency_code]) * amount_to_exchange:.2f} {to_currency_code.upper()}")
