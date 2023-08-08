import pytest

import pandas as pd

from rl_trader.common.decorators import rearranged
from rl_trader.common.exceptions import ValidationError


@pytest.mark.parametrize(
    ["return_index", "demanded_index"],
    [(["a", "b", "c"], ["a", "b"]), (["a", "b", "c"], ["a", "b", "c"])],
)
def test_rearranged_correctly_done(return_index: list[str], demanded_index: list[str]):
    @rearranged(output_schema=pd.Index(demanded_index))
    def func() -> pd.DataFrame:
        return pd.DataFrame([[0] * len(return_index)], columns=return_index)

    func()
    assert True  # no error raised


def test_rearranged_raises_error():
    @rearranged(output_schema=pd.Index(["a", "b"]))
    def func() -> pd.DataFrame:
        return pd.DataFrame([[0, 1]], columns=["b", "c"])

    with pytest.raises(ValidationError):
        func()
