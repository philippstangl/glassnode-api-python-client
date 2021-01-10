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


def is_not_btc_eth_ltc(asset):
    return True if asset != 'BTC' and asset != 'ETH' and asset != 'LTC' else False


def is_not_btc_eth(asset):
    return True if asset != 'BTC' and asset != 'ETH' else False


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
