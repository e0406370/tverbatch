from helpers import Tver, Messages
from helpers import validate_links

VALID_EPISODE_ID = Tver.TEST_EPISODE["valid"]["id"]
VALID_EPISODE_URL = Tver.get_episode_url(VALID_EPISODE_ID)

VALID_SERIES_ID_1 = Tver.TEST_SERIES["valid"]["id"]
VALID_SERIES_ID_2 = Tver.TEST_SERIES["valid_2"]["id"]
VALID_SERIES_URL_1 = Tver.get_series_url(VALID_SERIES_ID_1)
VALID_SERIES_URL_2 = Tver.get_series_url(VALID_SERIES_ID_2)

INVALID_ID = "abc123"
INVALID_URL = "https://www.google.com/"


# [validate_links][episodes] Valid links in URL format
def test_validate_links_episodes_valid_url():

    links = [
        VALID_EPISODE_URL
    ]
    expected = links

    assert validate_links(links).get_all() == expected, "[episodes] validate_links should capture all valid links (URL format)"


# [validate_links][episodes] Valid links in ID format
def test_validate_links_episodes_valid_id():

    links = [
        VALID_EPISODE_ID
    ]
    expected = [Tver.get_episode_url(link) for link in links]

    assert validate_links(links).get_all() == expected, "[episodes] validate_links should capture all valid links (ID format)"


# [validate_links][episodes] Mix of valid and invalid links
def test_validate_links_episodes_valid_invalid(caplog):

    links = [
        VALID_EPISODE_URL,
        INVALID_ID,
    ]
    expected = [VALID_EPISODE_URL]

    assert validate_links(links).get_all() == expected, "[episodes] validate_links should capture valid links but not invalid links"

    captured = caplog.text

    for link in set(links).difference(expected):
        assert Messages.WARN_INVALID_URL_ID % link in captured, "[episodes] Expected warning message for invalid link"


# [validate_links][series] Valid links in URL format
def test_validate_links_series_valid_url():

    links = [
        VALID_SERIES_URL_1,
        VALID_SERIES_URL_2,
    ]
    expected = links

    assert validate_links(links).get_all() == expected, "[series] validate_links should capture all valid links (URL format)"


# [validate_links][series] Valid links in ID format
def test_validate_links_series_valid_id():

    links = [
        VALID_SERIES_ID_1, 
        VALID_SERIES_ID_2
    ]
    expected = [Tver.get_series_url(link) for link in links]

    assert validate_links(links).get_all() == expected, "[series] validate_links should capture all valid links (ID format)"


# [validate_links][series] Mix of valid and invalid links
def test_validate_links_series_valid_invalid(caplog):

    links = [
        VALID_SERIES_URL_1,
        INVALID_ID,
    ]
    expected = [VALID_SERIES_URL_1]

    assert validate_links(links).get_all() == expected, "[series] validate_links should capture valid links but not invalid links"

    captured = caplog.text

    for link in set(links).difference(expected):
        assert Messages.WARN_INVALID_URL_ID % link in captured, "[series] Expected warning message for invalid link"


# [validate_links][mixed] Valid links in URL format
def test_validate_links_mixed_valid_url():

    links = [
        VALID_EPISODE_URL,
        VALID_SERIES_URL_1,
    ]
    expected = links

    assert validate_links(links).get_all() == expected, "[mixed] validate_links should capture all valid links (URL format)"


# [validate_links][mixed] Valid links in ID format
def test_validate_links_mixed_valid_id():

    links = [
        VALID_EPISODE_ID,
        VALID_SERIES_ID_1,
    ]
    expected = [Tver.get_episode_url(links[0]), Tver.get_series_url(links[1])]

    assert validate_links(links).get_all() == expected, "[mixed] validate_links should capture all valid links (ID format)"   


# [validate_links][mixed] Mix of valid and invalid links
def test_validate_links_mixed_valid_invalid(caplog):

    episodes = [
        VALID_EPISODE_URL,
        VALID_EPISODE_ID,
    ]
    series = [
        VALID_SERIES_URL_1,
        VALID_SERIES_ID_1,
    ]
    invalid = [
        INVALID_URL,
        INVALID_ID,
    ]

    links = [
        *episodes,
        *series,
        *invalid
    ]
    expected = [
        *[VALID_EPISODE_URL, VALID_EPISODE_URL],
        *[VALID_SERIES_URL_1, VALID_SERIES_URL_1]
    ]

    assert validate_links(links).get_all() == expected, "[mixed] validate_links should capture valid links but not invalid links"

    captured = caplog.text

    for link in invalid:
        assert Messages.WARN_INVALID_URL_ID % link in captured, "[mixed] Expected warning message for invalid link"


# [validate_links] Only invalid links
def test_validate_links_invalid_only(caplog):

    links = [
        INVALID_URL,
        INVALID_ID,
    ]
    expected = []

    assert validate_links(links).get_all() == expected, "validate_links should not capture any invalid links (both URL and ID formats)"

    captured = caplog.text

    for link in links:
        assert Messages.WARN_INVALID_URL_ID % link in captured, "Expected warning message for invalid link"