from abc import ABC, abstractmethod

import pandas as pd

from rl_trader.common.interface import ComponentBaseInterface


class DataFetcherInterface(ComponentBaseInterface, ABC):
    """
    The interface for data fetchers.
    """

    @abstractmethod
    def fetch_history_data(self, *, ticker: str, period: str) -> pd.DataFrame:
        """
        Fetch the data according to a given list of options.
        """
        ...

    @abstractmethod
    def _log(self, *, message: str, level: str) -> None:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        super().__repr__()
