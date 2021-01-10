import os
import requests
from .utils import *


class GlassnodeClient:
    def __init__(self, api_key=None, asset='BTC', interval='24h', currency='native', since=None, until=None):
        """
        Glassnode API client.

        :param asset: Asset to which the metric refers. (ex. BTC)
        :param interval: Temporal resolution of the data received. Can be '10m', '1h', '24h', '1w' or '1month'.
        :param currency: NATIVE, USD
        :param since: Start date as a string (ex. 2015-11-27)
        :param until: Start date as a string (ex. 2018-05-03)
        """
        self._api_key = ''
        if api_key:
            self._api_key = api_key
        else:
            self._api_key = os.environ.get('GLASSNODE_API_KEY')

        self._asset = asset
        self._interval = interval
        self._since = since
        self._until = until
        self._currency = currency

    @property
    def asset(self):
        return self._asset

    def get(self, endpoint, params=None):
        return self.__get(endpoint, params)

    def __prepare_request_params(self, params):
        p = dict()
        p['api_key'] = self._api_key
        p['a'] = self._asset
        p['i'] = self._interval

        if self._since is not None:
            try:
                p['s'] = unix_timestamp(self._since)
            except Exception as e:
                print(e)

        if self._until is not None:
            try:
                p['u'] = unix_timestamp(self._until)
            except Exception as e:
                print(e)

        # Set domain specific query parameters if available
        if params:
            if 'e' in p:
                p['e'] = params['e']
            if 'm' in p:
                p['m'] = params['m']

        return p

    def __get(self, endpoint, params):
        """
        Returns an object of time, value pairs for a metric from the Glassnode API.

        :param endpoint: Endpoint url corresponding to some metric (ex. '/v1/metrics/market/price_usd')
        :return: DataFrame of {'t' : datetime, 'v' : 'metric-value'} pairs
        """
        p = self.__prepare_request_params(params)
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
