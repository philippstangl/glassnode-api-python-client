from .utils import *
from .client import GlassnodeClient


class ETH2:
    def __init__(self, glassnode_client: GlassnodeClient):
        self.glassnode = glassnode_client

    def new_deposits(self):
        """
        The number transactions depositing 32 ETH to the ETH2 deposit contract.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingDepositsCount>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/eth2/staking_deposits_count'))

    def new_value_staked(self):
        """
        The amount of ETH transferred to the ETH2 deposit contract.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingVolumeSum>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/eth2/staking_volume_sum'))

    def new_validators(self):
        """
        The number of new validators (accounts) depositing 32 ETH to the ETH2 deposit contract.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingValidatorsCount>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/eth2/staking_validators_count'))

    def total_number_of_deposits(self):
        """
        The total number of transactions to the ETH2 deposit contract.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingTotalDepositsCount>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/eth2/staking_total_deposits_count'))

    def total_value_staked(self):
        """
        The amount of ETH that has been deposited to the ETH2 deposit contract,
        the current ETH balance on the ETH2 deposit contract.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingTotalVolumeSum>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/eth2/staking_total_volume_sum'))

    def total_number_of_validators(self):
        """
        The total number of unique validators (accounts) that have deposited 32 ETH to the ETH2 deposit contract.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingTotalValidatorsCount>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/eth2/staking_total_validators_count'))

    def phase_zero_staking_goal(self):
        """
        The percentage of the Phase 0 staking goal.
        `View in Studio:  <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingPhase0GoalPercent>`_

        :return: DataFrame
        """
        return response_to_dataframe(self.glassnode.get('/v1/metrics/eth2/staking_phase_0_goal_percent'))
