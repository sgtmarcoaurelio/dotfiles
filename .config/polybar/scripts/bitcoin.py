#!/usr/bin/env python

import requests

try:
    r = requests.get(
        'https://api.coinmarketcap.com/v1/ticker/bitcoin//?convert\=BRL');
    ticker = r.json()
    print("%{F#00EDFF}  %{F-} " + ticker[0]['price_usd'])

except Exception:
    print("%{F#555} %{F-}")
