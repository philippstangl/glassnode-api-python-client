from .utils import *
from .client import GlassnodeClient


class Protocols:
    def __init__(self, glassnode_client: GlassnodeClient):
        self.glassnode = glassnode_client

    def uniswap_transactions(self):
        """
        The total number of transactions that contains an interaction within Uniswap contracts.
        Includes Mint, Burn, and Swap events on the Uniswap core contracts.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=protocols.UniswapTransactionCount>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/protocols/uniswap_transaction_count'))

    def uniswap_liquidity(self):
        """
        The current liquidity on Uniswap.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=protocols.UniswapLiquidityLatest>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/protocols/uniswap_liquidity_latest'))

    def uniswap_volume(self):
        """
        The total volume traded on Uniswap.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=protocols.UniswapVolumeSum>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/protocols/uniswap_volume_sum'))
