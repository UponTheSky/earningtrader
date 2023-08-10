from __future__ import annotations

from typing import Mapping, Any, Sequence
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

from rl_trader.common.interface import ComponentBaseInterface
from rl_trader.storage import StorageInterface


class RLTradingModelInterface(ComponentBaseInterface, ABC):
    """
    The interface for RL trading models.
    """

    @abstractmethod
    def load_parameters(self, *, storage: StorageInterface, key: str) -> None:
        """
        Load the parameters of the current model.
        """
        ...

    @abstractmethod
    def set_parameters(self, *, parameters: Mapping[str, Any]) -> None:
        """
        Set the parameters of the current model.

        This is either for setting new ones or updating the existing ones.
        """
        ...

    @abstractmethod
    def save_parameters(self, *, storage: StorageInterface, key: str) -> None:
        """
        Save the parameters of the current model into the storage.
        """
        ...

    @abstractmethod
    def take_action(self, *, states: Sequence[State]) -> Action:
        """
        Take an action based on the current parameters and the states given.
        """
        ...

    @abstractmethod
    def earn_reward(self, *, reward: Reward) -> None:
        """
        Earn the reward as the result of the action taken, and update the parameter.
        """
        ...


@dataclass
class State(ABC):
    """
    A representation of a single unit of the current entire state.
    """

    ...


class Action(Enum, ABC):
    """
    The enumeration of the actions to be taken.
    """

    ...


@dataclass
class Reward(ABC):
    """
    The value of the reward earned as the result of the taken action.
    """
