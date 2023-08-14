from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class RLTradingModelInterface(ABC):
    """
    The interface for RL trading models.
    """

    _state: State

    @property
    def state(self) -> State:
        ...

    @abstractmethod
    def take_action(self) -> Action:
        """
        Take an action based on the current parameters and the state given.
        """
        ...

    @abstractmethod
    def earn_reward(self, *, reward: Reward) -> None:
        """
        Earn the reward as the result of the action taken, and update the parameter.
        """
        ...


class State(ABC):
    """
    A representation of a single unit of the current entire state.
    """

    ...


@dataclass(frozen=True)
class Action(ABC):
    """
    Actions to be taken by the algorithm.
    """

    ...


@dataclass(frozen=True)
class Reward(ABC):
    """
    The value of the reward earned as the result of the taken action.
    """

    ...
