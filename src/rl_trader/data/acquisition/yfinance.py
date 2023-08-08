from typing import Literal
import logging  # TODO: replace with the custom logger

import pandas as pd
import yfinance as yf

from ._interface import DataFetcherInterface


class YFinanceFetcher(DataFetcherInterface):
    """
    An adapter class for the yfinance package(https://github.com/ranaroussi/yfinance).

    After investing some time on this open source, we may switch to use the original
    APIs directly: see https://financeapi.net/.
    """

    _logger: logging.Logger  # TODO: replace with the custom logger

    def __init__(self) -> None:
        # TODO: add custom logger
        self._logger = logging.getLogger(self.__class__.__name__)

    def fetch_history_data(self, *, ticker: str, period: Literal["1d"]) -> pd.DataFrame:
        try:
            return yf.Ticker(ticker).history(period=period)

        except Exception as error:
            self._log(message=str(error), level="INFO")
            raise

    def _log(self, *, message: str, level: str) -> None:
        # TODO: use the custom logger
        return self._logger.info(message)

    def __repr__(self) -> str:
        # TODO: change this after more elaborations
        return f"Component '{self.__class__.__name__}'"
