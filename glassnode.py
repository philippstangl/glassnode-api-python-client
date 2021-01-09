import os
import requests
from utils import *


class GlassnodeClient:
    def __init__(self, asset='BTC', interval='24h', currency='native', since=None, until=None):
        """
        Glassnode API client.

        :param asset: Asset to which the metric refers. (ex. BTC)
        :param interval: Temporal resolution of the data received. Can be '10m', '1h', '24h', '1w' or '1month'.
        :param currency: NATIVE, USD
        :param since: Start date as a string (ex. 2015-11-27)
        :param until: Start date as a string (ex. 2018-05-03)
        """
        self._api_key = os.environ.get('GLASSNODE_API_KEY')
        self.a = asset
        self.i = interval
        self.s = since
        self.u = until
        self.c = currency

    def get(self, endpoint):
        """
        Returns an object of time, value pairs for a metric from the Glassnode API.

        :param endpoint: Endpoint url corresponding to some metric (ex. '/v1/metrics/market/price_usd')
        :return: DataFrame of {'t' : datetime, 'v' : 'metric-value'} pairs
        """
        p = dict()
        p['api_key'] = self._api_key
        p['a'] = self.a
        p['i'] = self.i

        if self.s is not None:
            try:
                p['s'] = unix_timestamp(self.s)
            except Exception as e:
                print(e)

        if self.u is not None:
            try:
                p['u'] = unix_timestamp(self.u)
            except Exception as e:
                print(e)

        r = requests.get(f'https://api.glassnode.com{endpoint}', params=p)
        try:
            r.raise_for_status()
        except Exception as e:
            print(e)
            print(r.text)

        return r.json()


if __name__ == "__main__":
    glassnode = GlassnodeClient(since='2021-01-01', until='2021-01-09')
    print(glassnode.get('/v1/metrics/market/price_usd'))
