from .utils import *
from .client import GlassnodeClient


class Indicators:
    def __init__(self, glassnode_client: GlassnodeClient):
        self.glassnode = glassnode_client

    def cvdd(self):
        """
        Cumulative Value-Days Destroyed (CVDD) is the ratio of the cumulative USD value of Coin Days Destroyed and
        the market age (in days). Historically, CVDD has been an accurate indicator for global Bitcoin market bottoms.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Cvdd>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/indicators/cvdd'))

    def reserve_risk(self):
        """
        When confidence is high and price is low, there is an attractive risk/reward to invest (Reserve Risk is low).
        When confidence is low and price is high then risk/reward is unattractive at that time (Reserve Risk is high).
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=indicators.ReserveRisk>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/indicators/reserve_risk'))

    @dataframe_with_inner_object
    def hash_ribbon(self):
        """
        The Hash Ribbon is a market indicator that assumes that Bitcoin tends to reach a bottom when miners capitulate,
        i.e. when Bitcoin becomes too expensive to mine relative to the cost of mining. The Hash Ribbon indicates that
        the worst of the miner capitulation is over when the 30d MA of the hash rate crosses above the 60d MA.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=indicators.HashRibbon>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/indicators/hash_ribbon'))

    def puell_multiple(self):
        """
        The Puell Multiple is calculated by dividing the daily issuance value of bitcoins (in USD)
        by the 365-day moving average of daily issuance value.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=indicators.PuellMultiple>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/indicators/puell_multiple'))

    def sopr(self):
        """
        The Spent Output Profit Ratio (SOPR) is computed by dividing the realized value (in USD)
        divided by the value at creation (USD) of a spent output. Or simply: price sold / price paid.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Sopr>`_

        :return: DataFrame
        """
        if is_not_btc_eth_ltc(self.glassnode.asset):
            return None
        return response_to_dataframe(self.glassnode.get('/v1/metrics/indicators/sopr'))

    def asopr(self):
        """
        Adjusted SOPR is SOPR ignoring all outputs with a lifespan of less than 1 hour.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=indicators.SoprAdjusted>`_

        :return: DataFrame
        """
        if is_not_btc_eth(self.glassnode.asset):
            return None
        return response_to_dataframe(self.glassnode.get('/v1/metrics/indicators/sopr_adjusted'))

    def net_unrealized_profit_loss(self):
        """
        Net Unrealized Profit/Loss is the difference between Relative Unrealized Profit/Loss.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=indicators.NetUnrealizedProfitLoss>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/indicators/net_unrealized_profit_loss'))


if __name__ == "__main__":
    indicator = Indicators(GlassnodeClient(since='2021-01-01', until='2021-01-09'))
    print(indicator.cvdd())
