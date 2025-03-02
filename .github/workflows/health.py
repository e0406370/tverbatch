from helpers.constants import Tver
import requests, sys


def check_response(url: str) -> bool:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Success: {url} is reachable.")
            return True
        else:
            print(f"Warning: {url} returned status code {response.status_code}.")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return False


if __name__ == "__main__":
    success = check_response(Tver.BASE_URL)
    sys.exit(0 if success else 1)
