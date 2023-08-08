from typing import TypeVar, Callable
import functools

import pandas as pd

from .exceptions import ValidationError


OutputSchema = TypeVar("OutputSchema", bound=pd.Index)


def rearranged(
    *, output_schema: OutputSchema
) -> Callable[[Callable[..., pd.DataFrame]], Callable[..., pd.DataFrame]]:
    def _decorator(func: Callable[..., pd.DataFrame]) -> Callable[..., pd.DataFrame]:
        @functools.wraps(func)
        def _wrapped(*args, **kwargs) -> pd.DataFrame:
            return_value = func(*args, **kwargs)

            if not output_schema.difference(return_value.columns).empty:
                raise ValidationError(
                    "There are missing fields in the returned dataframe "
                    "compared to the provided schema"
                )

            return_value.drop(
                columns=return_value.columns.difference(output_schema), inplace=True
            )
            return return_value

        return _wrapped

    return _decorator
