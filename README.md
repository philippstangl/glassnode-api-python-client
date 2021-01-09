# glassnode-api-python-client
This is my own take on the official Python client library for Glassnode's API – https://docs.glassnode.com

I'm currently using the API for my own project and had to overwrite the official python client. 
I thought sharing my own version of it may help some of you.

## Quick Start

### API Key

1. Get your API key from your [Glassnode account](https://studio.glassnode.com/settings/api).

2. Add your API key to your environment variables by running:
   
    `export GLASSNODE_API_KEY=<YOUR-KEY>`

### Example Usage

In the following example, we get several Bitcoin indicators and market data for December 2020.

```
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
