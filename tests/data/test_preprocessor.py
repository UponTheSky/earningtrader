import pytest

import pandas as pd

from rl_trader.data.preprocessing.preprocessor import DataPreprocessor
from rl_trader.common.exceptions import ValidationError


@pytest.fixture
def preprocessor() -> DataPreprocessor:
    return DataPreprocessor()


@pytest.mark.parametrize(
    ["input_index", "data_schema"],
    [(["a", "b", "c"], ["a", "b"]), (["a", "b", "c"], ["a", "b", "c"])],
)
def test_rearranged_correctly_done(
    preprocessor: DataPreprocessor, input_index: list[str], data_schema: list[str]
):
    preprocessor.rearrange_raw_data(
        input=pd.DataFrame([[0] * len(input_index)], columns=input_index),
        data_schema=pd.Index(data_schema),
    )


@pytest.mark.parametrize(
    ["input_index", "data_schema"],
    [(["a", "b"], ["b", "c"]), (["d"], ["a", "b", "c"])],
)
def test_rearranged_raises_error(
    preprocessor: DataPreprocessor, input_index: list[str], data_schema: list[str]
):
    with pytest.raises(ValidationError):
        preprocessor.rearrange_raw_data(
            input=pd.DataFrame([[0] * len(input_index)], columns=input_index),
            data_schema=pd.Index(data_schema),
        )
