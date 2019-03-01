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

tap = liquidtap.Client()
tap.pusher.connect()

channel = tap.subscribe("product_cash_usdjpy_5")

channel.bind('updated', update_callback)
```


# Authentication
### Authenticate on initialization
```python

import liquidtap

tap = liquidtap.Client("insert token id", "insert token secret")
tap.pusher.connect()

# Refer to profile page for user_id: https://app.liquid.com/settings/profile
channel = tap.subscribe("user_<user_id>")

channel.bind('updated', update_callback)
```
