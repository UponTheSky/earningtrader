from typing import Literal, Any
from abc import ABC, abstractmethod, abstractstaticmethod

import pandas as pd

from rl_trader.common.interface import ComponentBaseInterface


class DataPreprocessorInterface(ComponentBaseInterface, ABC):
    """
    The interface for the data preprocessing components.
    """

    @abstractstaticmethod
    def rearrange_raw_data(
        *, input: pd.DataFrame, data_schema: pd.Index
    ) -> pd.DataFrame:
        """
        Check whether the input data satisfies the schema provided.

        Otherwise, it will raise ValidationError.
        """
        ...

    @abstractstaticmethod
    def handle_missing_values(
        *,
        input: pd.DataFrame,
        option: Literal["exclude", "replace"],
        replace_value: Any,
    ) -> pd.DataFrame:
        """
        Handles missing values in the pd.DataFrame(NaN).

        So this function is a wrapper of the more general APIs explained here
        in this guide: https://pandas.pydata.org/docs/user_guide/missing_data.html
        """
        ...

    @abstractmethod
    def _log(self, *, message: str, level: str) -> None:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        super().__repr__()
