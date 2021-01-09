from utils import *
from glassnode import GlassnodeClient


class Market:
    def __init__(self, glassnode_client: GlassnodeClient):
        self.glassnode = glassnode_client

    def price(self):
        """
        The asset's price in USD.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceUsd>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/price_usd'))

    @dataframe_with_inner_object
    def price_ohlc(self):
        """
        OHLC candlestick chart of the asset's price in USD.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceUsdOhlc>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/price_usd_ohlc'))

    def price_drawdown_from_ath(self):
        """
        The percent drawdown of the asset's price from the previous all-time high.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceDrawdownRelative>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/price_drawdown_relative'))

    def marketcap(self):
        """
        The market capitalization (or network value) is defined as
        the product of the current supply by the current USD price.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.MarketcapUsd>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/marketcap_usd'))

    def mvrv_ratio(self):
        """
        MVRV is the ratio between market cap and realised cap.
        It gives an indication of when the traded price is below a “fair value”.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.Mvrv>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/mvrv'))

    def realized_cap(self):
        """
        Realized Cap values different part of the supplies at different prices (instead of using current daily close).
        Specifically, it is computed by valuing each UTXO by the price when it was last moved.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.MarketcapRealizedUsd>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/marketcap_realized_usd'))

    def mvrv_z_score(self):
        """
        The MVRV Z-Score is used to assess when Bitcoin is over/undervalued relative to its "fair value".
        When market value is significantly higher than realized value, it has historically indicated a market top
        (red zone), while the opposite has indicated market bottoms (green zone).
        Technically, MVRV Z-Score is defined as the ratio between the difference of market cap and realized cap,
        and the standard deviation of market cap, i.e. (market cap – realized cap) / std(market cap).
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.MvrvZScore>`_

        :return:
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/mvrv_z_score'))

    def sth_mvrv(self):
        """
        Short Term Holder MVRV (STH-MVRV) is MVRV that takes into account only UTXOs younger than 155 days and
        serves as an indicator to assess the behaviour of short term investors.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.MvrvLess155>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/mvrv_less_155'))

    def lth_mvrv(self):
        """
        Long Term Holder MVRV (LTH-MVRV) is MVRV that takes into account only UTXOs with a lifespan of at least 155 days
        and serves as an indicator to assess the behaviour of long term investors
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.MvrvMore155>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/mvrv_more_155'))

    def realized_price(self):
        """
        Realized Price is the Realized Cap divided by the current supply.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceRealizedUsd>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/market/price_realized_usd'))


if __name__ == "__main__":
    market = Market(GlassnodeClient(since='2021-01-01', until='2021-01-09'))
    print(market.realized_price())
