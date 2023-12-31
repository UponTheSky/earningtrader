import pathlib

import pytest

from earningtrader.controller.bernoulli_ts_simulator import (
    BernTSControllerBuilder,
    BernTSController,
)


@pytest.fixture
def controller(tmp_path: pathlib.Path) -> BernTSController:
    builder = BernTSControllerBuilder()
    builder.initialize(logfile_dir=str(tmp_path))
    builder.set_data_fetcher()
    builder.set_data_preprocessor()
    builder.set_trading_model()
    builder.set_storage(db_path=str(tmp_path / "temp_storage.shelve"))
    builder.set_trader()

    return builder.controller()


def test_entier_simulation(controller: BernTSController):
    for _ in range(10):  # 10-days trading simulator
        action = controller.choose_action()
        reward = controller.make_trade(action=action)
        controller.save_reward(reward=reward)

    storage = controller._storage
    reward_history = storage.load_data(key="reward_history")

    assert len(reward_history) == 10
    assert all(map(lambda x: 0 <= x.reward <= 1.0, reward_history))
