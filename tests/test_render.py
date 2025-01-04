import pytest
from helpers import *
from tver import render_tver


@pytest.fixture(scope="session")
def shared_driver():

    with make_webdriver() as driver:
        yield driver


def test_render_tver_with_valid_series(shared_driver):

    series_url = Tver.get_series_url(Tver.SERIES_ID["valid"])
    render_status = render_tver(shared_driver, series_url)

    assert render_status is True, "render_tver should return True for valid series"


def test_render_tver_with_invalid_series(shared_driver, capsys):

    series_url = Tver.get_series_url(Tver.SERIES_ID["invalid"])
    render_status = render_tver(shared_driver, series_url)

    assert Messages.ERROR_INVALID_SERIES_ID in capsys.readouterr().out, "Expected error message for invalid series"
    assert render_status is False, "render_tver should return False for invalid series"


def test_render_tver_with_not_airing_series(shared_driver, capsys):

    series_url = Tver.get_series_url(Tver.SERIES_ID["not_airing"])
    render_status = render_tver(shared_driver, series_url)

    assert Messages.ERROR_NOT_AIRING_SERIES in capsys.readouterr().out, "Expected error message for not airing series"
    assert render_status is False, "render_tver should return False for not airing series"
