from .utils import *
from .client import GlassnodeClient


class Mining:
    def __init__(self, glassnode_client: GlassnodeClient):
        self.glassnode = glassnode_client

    def difficulty(self):
        """
        The current estimated number of hashes required to mine a block. Values are denoted in raw hashes.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.DifficultyLatest>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/difficulty_latest'))

    def hash_rate(self):
        """
        The average estimated number of hashes per second produced by the miners in the network.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.HashRateMean>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/hash_rate_mean'))

    def miner_revenue_total(self, miner=None):
        """
        The total miner revenue, i.e. fees plus newly minted coins.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.RevenueSum>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/revenue_sum', {'m': miner}))

    def miner_revenue_fees(self):
        """
        The percentage of miner revenue derived from fees, i.e. fees divided by fees plus minted coins.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.RevenueFromFees>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/revenue_from_fees'))

    def miner_revenue_block_rewards(self, miner=None):
        """
        The total amount of newly minted coins, i.e. block rewards.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.VolumeMinedSum>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/volume_mined_sum', {'m': miner}))

    def miner_outflow_multiple(self, miner=None):
        """
        The Miner Outflow Multiple indicates periods where the amount of bitcoins flowing out of
        miner addresses is high with respect to its historical average.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.MinersOutflowMultiple>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/miners_outflow_multiple', {'m': miner}))

    def thermocap(self):
        """
        Aggregate security spend, or "Thermocap", is the aggregated amount of coins paid to miners
        and serves as a proxy to mining resources spent. It serves a measure of the true capital flow
        into Bitcoin and is computed as the aggregate coinbase transactions multiplied by the price
        in USD at the time they were mined.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.Thermocap>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/thermocap'))

    def market_cap_to_thermocap_ratio(self):
        """
        The Marketcap to Thermocap Ratio is simply defined as Marketcap / Thermocap, and can be used
        to assess if the asset's price is currently trading at a premium with respect to total security spend by miners.
        The ratio is adjusted to account for the increasing circulating supply over time.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.MarketcapThermocapRatio>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/marketcap_thermocap_ratio'))

    def miner_unspent_supply(self):
        """
        The total mount of coins in coinbase transactions that have never been moved.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=BTC&m=mining.MinersUnspentSupply>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/mining/miners_unspent_supply'))

    def miner_names(self, endpoint='revenue_sum'):
        """
        Returns a list of miner names for a given endpoint.

        :param endpoint: Available endpoints: revenue_sum, volume_mined_sum, miners_outflow_multiple
        :return: List
        """
        miners = self.glassnode.get(f'/v1/metrics/mining/{endpoint}/miners')
        return miners[self.glassnode.asset]
