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

In the following example, we get CVDD and Price data per day for Bitcoin in the given timeframe.

```
from glassnode import GlassnodeClient
from indicators import Indicators
from market import Market

glassnode = GlassnodeClient(since='2021-01-01', until='2021-01-09')

indicators = Indicators(glassnode)
indicators.cvdd()

market = Market(glassnode)
market.price()
```

For a complete list of all available metric endpoints and query parameters please visit [docs.glassnode.com](https://docs.glassnode.com).

## Further Information

* [API documentation](https://docs.glassnode.com/)
* [Overview of metrics and restrictions](https://glassnode.com/metrics)
