import calendar
import pandas as pd

from datetime import datetime


def unix_timestamp(date_str):
    """
    Returns a unix timestamp to a given date string.

    :param date_str: Date in string format (ex. '2021-01-01').
    :return: Int Unix-timestamp.
    """
    dt_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return calendar.timegm(dt_obj.utctimetuple())


def is_btc(symbol):
    return symbol == 'BTC'


def is_ltc(symbol):
    return symbol == 'LTC'


def is_eth(symbol):
    return symbol == 'ETH'


def is_erc20(symbol, g_client):
    erc20_tokens = [asset['symbol'] for asset in g_client.get('/v1/metrics/assets') if 'erc20' in asset['tags']]
    return symbol in erc20_tokens


def is_not_btc_eth(symbol):
    return True if not is_btc(symbol) and not is_eth(symbol) else False


def is_not_btc_eth_ltc(symbol):
    return True if is_not_btc_eth(symbol) and not is_ltc(symbol) else False


def is_not_btc_ltc_eth_erc20(symbol, g_client):
    return True if is_not_btc_eth_ltc(symbol) and not is_erc20(symbol, g_client) else False


def response_to_dataframe(response):
    """
    Returns DataFrame from a response objects (ex. {"t":1604361600,"v":0.002}).

    :param response: Response from API.
    :return: DataFrame.
    """
    try:
        df = pd.DataFrame(response)
        df.set_index('t', inplace=True)
        df.index = pd.to_datetime(df.index, unit='s')
        df.index.name = None
        df.sort_index(ascending=False, inplace=True)
        return df
    except Exception as e:
        print(e)


def dataframe_with_inner_object(func):
    def wrapper(*args, **kwargs):
        df = func(*args, **kwargs)
        return pd.concat([df.drop(['o'], axis=1), df['o'].apply(pd.Series)], axis=1)
    return wrapper
