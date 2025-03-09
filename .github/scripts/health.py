from helpers.constants import Tver
import requests, sys

URL_LIST = [
    Tver.BASE_URL,
    Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"]),
    Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]),
]


def is_reachable(url: str) -> bool:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[Success] {url} is reachable.")
            return True
        else:
            print(f"[Warning] {url} returned status code {response.status_code}.")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[Error] {e}")
        return False


if __name__ == "__main__":
    sys.exit(0 if all(is_reachable(url) for url in URL_LIST) else 1)
