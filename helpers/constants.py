class Tver:
    BATCH_FILE = "tver.txt"
    BASE_URL = "https://tver.jp"

    VALID_EPISODE_URL = r"https?://(?:www\.)?tver\.jp/episodes/(ep[a-z0-9]{8})"
    VALID_EPISODE_ID = r"ep[a-z0-9]{8}"

    VALID_SERIES_URL = r"https?://(?:www\.)?tver\.jp/series/(sr[a-z0-9]{8})"
    VALID_SERIES_ID = r"sr[a-z0-9]{8}"
    
    TEST_EPISODE = {
        "valid": {
            "id": "ep0mnciv96",
            "title": "#1154「屋久島の山姫（後編）」",
            "broadcast": "2月22日(土)放送分",
            "end": "3月1日(土)17:59 終了予定"
        },
        "invalid": {
            "id": "ep12345678"
        }
    }
    TEST_EPISODE_END_DATETIME_REGEX = r"(\d+)月(\d+)日.*?(\d{2}:\d{2})"

    TEST_SERIES = {
        "valid": {
            "id": "srtxft431v",
            "name": "名探偵コナン"
        },
        "valid_2": {
            "id": "srtsxzl3si", 
            "name": "ドラえもん"
        },
        "invalid": {
            "id": "sr12345678",
            "name": "invalid"
        },
        "invalid_2": {
            "id": "sr23456789",
            "name": "invalid_2"
        },
        "not_airing": {
            "id": "sre9gy29cj",
            "name": "家族ゲーム"
        },
        "not_airing_2": {
            "id": "srs8ad9qnl",
            "name": "名前をなくした女神"
        },
    }

    TOTAL_CHAR_1 = "全"
    TOTAL_CHAR_2 = "件"

    @classmethod
    def get_episode_url(cls, episode_id: str) -> str:
        return f"{cls.BASE_URL}/episodes/{episode_id}"

    @classmethod
    def get_series_url(cls, series_id: str) -> str:
        return f"{cls.BASE_URL}/series/{series_id}"


class ClassNames:
    ERROR_MODAL = "error-modal_message"
    LOAD_ICON = "loading_box"

    SERIES_TITLE = "series-main_title"
    SERIES_DESCRIPTION = "description_container"

    EPISODE_LIST_EMPTY = "episode-live-list-column_empty"
    EPISODE_LIST = "episode-live-list-column_episodeList"

    EPISODE_ROW = "episode-row_container"
    EPISODE_ROW_TITLE = "episode-row_title"
    EPISODE_ROW_BROADCAST_DATE = "episode-row_broadcastDateLabel"
    EPISODE_ROW_END_DATE = "episode-row_endAt"


class Messages:
    USAGE = """
    Description:
        This script extracts episode links from series currently streaming on TVer and then downloads the corresponding episodes.
        
    Usage: 
        python tver.py URL [URL...]
        
        URL can be one of the following formats:
        - episode_url => https://tver.jp/episodes/ep12345678
        - episode_id => ep12345678 
        - series_url => https://tver.jp/series/sr12345678
        - series_id => sr12345678
        
    Repository:
        https://github.com/e0406370/tverbatch
    """

    WARNING_INVALID_URL_ID = "Invalid URL/ID skipped - %s"
    WARNING_NO_VALID_LINKS = "No valid links were found. Please provide at least one valid episode or series link."

    ERROR_INVALID_EPISODE_ID = "The provided episode ID is invalid!"
    ERROR_INVALID_SERIES_ID = "The provided series ID is invalid!"
    ERROR_NOT_AIRING_SERIES = "This series is currently not airing!"

    PROCESS_EPISODE = "Processing episode %s"
    PROCESS_EPISODE_COMPLETE = "Added to batch file."
    PROCESS_SERIES = "Processing series %s"
    PROCESS_DOWNLOAD = "Starting download..."

    SCRIPT_START = "Starting script..."
    SCRIPT_EXIT = "Exiting script..."
    SCRIPT_COMPLETE = "Script completed."
