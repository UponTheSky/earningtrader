from abc import ABC, abstractmethod

from rl_trader.data.acquisition import DataFetcherInterface
from rl_trader.data.preprocessing import DataPreprocessorInterface
from rl_trader.model import (
    StateInterface,
    ActionInterface,
    RewardInterface,
    RLTradingModelInterface,
)
from rl_trader.storage import StorageInterface
from rl_trader.trader import TraderInterface


class ControllerInterface(ABC):
    """
    The interface for the central component controlling the other components.
    """

    _data_fetcher: DataFetcherInterface
    _data_preprocessor: DataPreprocessorInterface
    _actions: set[ActionInterface]
    _model: RLTradingModelInterface
    _trader: TraderInterface
    _storage: StorageInterface

    @abstractmethod
    def observe_state(self) -> StateInterface:
        """
        A factory method for converting external data into a defined state.
        """
        ...

    @abstractmethod
    def choose_action(self, *, observed_state: StateInterface) -> ActionInterface:
        """
        Given the observed state, choose the action using the RL model.
        """
        ...

    @abstractmethod
    def make_trade(self, *, action: ActionInterface) -> RewardInterface:
        """
        Take the action determined from the model, and
        return the reward from the actual trading.
        """
        ...

    @abstractmethod
    def save_reward(self, reward: RewardInterface) -> None:
        """
        Save the reward to assess the performance of the model.
        """
        ...
