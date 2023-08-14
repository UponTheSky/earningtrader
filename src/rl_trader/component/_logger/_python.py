from typing import overload
import logging

from ._interface import LoggerInterface


class PythonFileLogger(LoggerInterface):
    _logger = logging.Logger

    def __init__(self, *, logger_name: str, filepath: str, message_format: str) -> None:
        self._logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler(filename=filepath, encoding="utf-8")
        file_handler.setFormatter(fmt=logging.Formatter(fmt=message_format))
        file_handler.setLevel(level=logging.DEBUG)

        self._logger.addHandler(file_handler)

    @overload
    def log(self, *, message: str, log_level: int) -> None:
        ...

    @overload
    def log(self, *, message: Exception, log_level: int) -> None:
        ...

    def log(self, *, message, log_level) -> None:
        if isinstance(message, Exception):
            self._logger.exception(level=log_level, msg=message)

        else:
            self._logger.log(level=log_level, msg=message)
