from helpers.actions import get_element_attribute, get_element_text, make_webdriver, wait_element_visible
from helpers.constants import Tver
from helpers.locators import Locators
from helpers.utils import re

from datetime import datetime
import pytz


# Update details in TEST_EPISODE
def update_test_episode():

    with make_webdriver() as driver:

        driver.get(Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]))

        wait_element_visible(driver, Locators.EPISODE_ROW)

        episode_id = get_element_attribute(driver, Locators.EPISODE_ROW, "href").partition("episodes/")[2]
        episode_title = get_element_text(driver, Locators.EPISODE_ROW_TITLE)
        episode_broadcast_date = get_element_text(driver, Locators.EPISODE_ROW_BROADCAST_DATE)
        episode_end_date = get_element_text(driver, Locators.EPISODE_ROW_END_DATE)

    with open("helpers/constants.py", "r", encoding="utf-8") as file:
        contents = file.read()

    updated_test_episode = re.sub(
        r'TEST_EPISODE\s*=\s*\{.*?\}',
        f'''TEST_EPISODE = {{
        "valid": {{
            "id": "{episode_id}",
            "title": "{episode_title}",
            "broadcast": "{episode_broadcast_date}",
            "end": "{episode_end_date}"
        }}''',
        contents,
        flags=re.DOTALL
    )

    with open("helpers/constants.py", "w", encoding="utf-8") as file:
        file.write(updated_test_episode)


# Checks if the current date in JST is after the end date in TEST_EPISODE
def need_update_test_episode():

    current_date = f"{datetime.now(pytz.timezone('Japan')):%m-%dT%H:%M}"
    end_date = format_test_episode_end_date()

    return current_date > end_date


# Format end date in TEST_EPISODE to MM-DDTHH:MM
def format_test_episode_end_date():

    match = re.search(Tver.TEST_EPISODE_END_DATETIME_REGEX, Tver.TEST_EPISODE["valid"]["end"])
    month = match.group(1).zfill(2)
    day = match.group(2).zfill(2)
    time = match.group(3)

    return f"{month}-{day}T{time}"


if __name__ == "__main__":

    if need_update_test_episode():
        update_test_episode()