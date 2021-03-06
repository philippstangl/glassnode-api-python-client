[![Glassnode](https://insights.glassnode.com/content/images/size/w2000/2019/06/medium---cover-intro-3.jpg)](http://glassnode.com/)

# Glassnode Python Client
Unofficial Python client library for Glassnode's API – https://docs.glassnode.com

## Quick Start

### API Key

1. Get your API key from your [Glassnode account](https://studio.glassnode.com/settings/api).

2. Add your API key to your environment variables by running:
   
    `export GLASSNODE_API_KEY=<YOUR-KEY>`

### Example Usage

In the following example, we get several Bitcoin indicators and market data for December 2020.
(Currently, the client returns a Pandas DataFrame as result.)

```python
from glassnode import GlassnodeClient, Indicators, Market

btc_dec_2020 = GlassnodeClient(asset='BTC', since='2020-12-01', until='2020-12-31')

indicators = Indicators(btc_dec_2020)
indicators.cvdd()
indicators.sopr()

market = Market(btc_dec_2020)
market.price()
market.marketcap()
```

For a complete list of all available metric endpoints and query parameters please visit [docs.glassnode.com](https://docs.glassnode.com).

## Further Information

* [API documentation](https://docs.glassnode.com/)
* [Overview of metrics and restrictions](https://glassnode.com/metrics)
