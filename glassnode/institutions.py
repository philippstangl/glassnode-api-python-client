from .utils import *
from .client import GlassnodeClient


class Institutions:
    """
        Institutions class.

        Methods
        -------
        __init__(glassnode_client):
            Constructs an Institutions object.
        grayscale_holdings():
            Returns the amount of Grayscale holdings.
        grayscale_flows():
            Returns the amount of funds flowing from/to the Grayscale trust.
        grayscale_premium():
            Returns the premium in the total value of shares to the NAV of the trust holdings.
        grayscale_aum():
            Returns the amount of Grayscale's assets under management.
        grayscale_market_price():
            Returns the market price per share in the Grayscale trust.
    """
    def __init__(self, glassnode_client: GlassnodeClient):
        self._gc = glassnode_client

    def grayscale_holdings(self) -> pd.DataFrame:
        """
        The amount of Grayscale holdings of the selected asset.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=institutions.GrayscaleHoldingsSum>`_
        """
        endpoint = '/v1/metrics/institutions/grayscale_holdings_sum'
        if not is_supported_by_endpoint(self._gc, endpoint):
            return pd.DataFrame()

        return response_to_dataframe(self._gc.get(endpoint))

    def grayscale_flows(self) -> pd.DataFrame:
        """
        The amount of funds flowing from/to the Grayscale trust of the selected asset.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=institutions.GrayscaleFlowsSum>`_
        """
        endpoint = '/v1/metrics/institutions/grayscale_flows_sum'
        if not is_supported_by_endpoint(self._gc, endpoint):
            return pd.DataFrame()

        return response_to_dataframe(self._gc.get(endpoint))

    def grayscale_premium(self) -> pd.DataFrame:
        """
        The premium in the total value of shares to the Net Asset Value (NAV)
        of the trust holdings of the selected asset.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=institutions.GrayscalePremiumPercent>`_
        """
        endpoint = '/v1/metrics/institutions/grayscale_premium_percent'
        if not is_supported_by_endpoint(self._gc, endpoint):
            return pd.DataFrame()

        return response_to_dataframe(self._gc.get(endpoint))

    def grayscale_aum(self) -> pd.DataFrame:
        """
        The amount of Grayscale's assets under management of the selected asset.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=institutions.GrayscaleAumSum>`_
        """
        endpoint = '/v1/metrics/institutions/grayscale_aum_sum'
        if not is_supported_by_endpoint(self._gc, endpoint):
            return pd.DataFrame()

        return response_to_dataframe(self._gc.get(endpoint))

    def grayscale_market_price(self) -> pd.DataFrame:
        """
        The market price per share in the Grayscale trust of the selected asset.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=institutions.GrayscaleMarketPriceUsd>`_
        """
        endpoint = '/v1/metrics/institutions/grayscale_market_price_usd'
        if not is_supported_by_endpoint(self._gc, endpoint):
            return pd.DataFrame()

        return response_to_dataframe(self._gc.get(endpoint))
