from unittest.mock import Mock, patch
from helpers import Driver, Tver, Locators, ClassNames, Messages
from tver import render_tver_series, filter_tver
import pytest


@pytest.fixture(scope="session", autouse=True)
def shared_driver():

    with Driver():
        yield


# [filter_tver] Verify filter_tver returns early without message when skip_filter is set to True
def test_filter_tver_skipped_by_flag():

    series_url = Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])
    mock_action = Mock()

    with patch("helpers.Driver.get_elements", side_effect=lambda *args: mock_action()):
        render_tver_series(series_url, skip_filter=True)

    mock_action.assert_not_called()


# [filter_tver] Verify filter_tver returns early with message when only default options are present
def test_filter_tver_default_options_only(caplog):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["valid_3"]["id"])
    render_tver_series(series_url, skip_filter=False)

    captured = caplog.text
    assert Messages.FILTER_SKIP in captured
    assert Tver.FILTER_OPTION_ALL not in captured


# [filter_tver] Verify filter_tver works properly when additional options are present
def test_filter_tver_additional_options(caplog):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["valid_2"]["id"])
    render_tver_series(series_url, skip_filter=True)

    options_list = Driver.get_elements(Locators.FILTER_BUTTON)
    options_count = len(options_list)

    initial_episode_count = len(Driver.get_elements(Locators.EPISODE_ROW))

    with patch("builtins.input", side_effect=["a", "1"]):
        filter_tver(skip_filter=False)

        captured = caplog.text

        assert Messages.FILTER_SKIP not in captured
        assert Tver.FILTER_OPTION_ALL in captured
        
        assert Messages.ERR_INVALID_INPUT_NOT_A_NUMBER in captured
        
    caplog.clear()
    
    with patch("builtins.input", side_effect=[str(options_count + 1), "1"]):
        filter_tver(skip_filter=False)

        captured = caplog.text
        
        assert Messages.FILTER_SKIP not in captured
        assert Tver.FILTER_OPTION_ALL in captured

        assert Messages.ERR_INVALID_INPUT_OUT_OF_RANGE % options_count in captured
        
    caplog.clear()

    with patch("builtins.input", side_effect=[str(options_count)]):
        filter_tver(skip_filter=False)

        Driver.wait_element_has_class(options_list[options_count - 1], ClassNames.FILTER_BUTTON_ACTIVE)
        updated_episode_count = len(Driver.get_elements(Locators.EPISODE_ROW))
        
        captured = caplog.text

        assert Messages.FILTER_SKIP not in captured
        assert Tver.FILTER_OPTION_ALL in captured

        assert updated_episode_count < initial_episode_count