# LiquidTap Python Client
To manage API tokens, refer to:
[https://app.liquid.com/settings/api-tokens](https://app.liquid.com/settings/api-tokens)

To learn more about Liquid Api token management, see the help links below:
[https://help.liquid.com/connect-to-liquid-via-api](https://help.liquid.com/connect-to-liquid-via-api)


# Getting Started

```
pip3 install liquidtap
```
The library can connect to public channels without token credentials.
```python
import liquidtap

def update_callback(data):
    print(data)

def on_connect(data):
    tap.pusher.subscribe("price_ladders_cash_btcjpy_buy").bind('updated', update_callback)

if __name__ == "__main__":
    tap = liquidtap.Client()
    tap.pusher.connection.bind('pusher:connection_established', on_connect)
    tap.pusher.connect()

```


# Authentication
### Authenticate on initialization
```python

import liquidtap

def update_callback(data):
    print(data)

def on_connect(data):
    print(data)
    tap.pusher.subscribe("price_ladders_cash_btcjpy_buy").bind('updated', update_callback)

if __name__ == "__main__":
    tap = liquidtap.Client("insert token id", "insert token secret")
    tap.pusher.connection.bind('pusher:connection_established', on_connect)
    tap.pusher.connect()

```
