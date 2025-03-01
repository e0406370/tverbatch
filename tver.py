"""
    Extracts links from one or more series currently streaming on TVer into a text file, using Selenium and Beautiful Soup.
    Afterwards, it uses yt-dlp internally to download the episodes based on the extracted links. 
"""

from helpers import *
from bs4 import BeautifulSoup
import yt_dlp


def render_tver_episode(episode: str) -> bool:

    Driver.get_instance().get(episode)

    if Driver.is_element_visible(Locators.ERROR_MODAL):
        Logger.err(Messages.ERR_INVALID_EPISODE_ID)
        return False

    return True


def render_tver_series(series: str) -> bool:

    Driver.get_instance().get(series)

    if Driver.is_element_visible(Locators.ERROR_MODAL):
        Logger.err(Messages.ERR_INVALID_SERIES_ID)
        return False

    Driver.wait_element_invisible(Locators.LOAD_ICON)

    if Driver.is_element_visible(Locators.EPISODE_LIST_EMPTY):
        Logger.err(Messages.ERR_NOT_AIRING_SERIES)
        return False

    Driver.wait_element_visible(Locators.EPISODE_LIST)

    filter_tver()

    return True


def filter_tver() -> None:

    if Driver.is_element_visible(Locators.TERMS_MODAL):
        Driver.click_element_loc(Locators.TERMS_MODAL)
        Driver.zoom_browser()

    filter_options = Driver.get_elements(Locators.FILTER_BUTTON)
    filter_size = len(filter_options)
    filter_lines = "\n".join((f'{idx + 1}. {opt.text}' for idx, opt in enumerate(filter_options)))

    Logger.info(Messages.FILTER_OPTIONS % filter_lines)
    while True:
        given_input = input(Messages.FILTER_PROMPT % filter_size)

        try:
            given_input = int(given_input)

            if 1 <= given_input <= filter_size:
                break

            else:
                Logger.err(Messages.ERR_INVALID_INPUT_OUT_OF_RANGE % filter_size)

        except ValueError:
            Logger.err(Messages.ERR_INVALID_INPUT_NOT_A_NUMBER)

    Driver.click_element_ele(filter_options[given_input - 1])


def scrape_tver() -> None:

    html = Driver.get_instance().page_source
    soup = BeautifulSoup(html, "html.parser")

    series_title = soup.select_one(css_selector_class_starts_with(ClassNames.SERIES_TITLE)).get_text()
    episodes = [
        Episode(
            (
                Tver.BASE_URL + href
            ),
            (
                date.get_text()
                if (date := episode_container.select_one(css_selector_class_starts_with(ClassNames.EPISODE_ROW_BROADCAST_DATE)))
                else ""
            ),
            (
                title.get_text()
                if (title := episode_container.select_one(css_selector_class_starts_with(ClassNames.EPISODE_ROW_TITLE)))
                else ""
            )
        )
        for episode_container in soup.select(css_selector_class_starts_with(ClassNames.EPISODE_ROW))
        if (href := episode_container.get("href")) and "episodes" in href
    ]

    Logger.info(f"{series_title} [{len(episodes)}]")
    for epi in episodes: Logger.info(str(epi))

    with open(Tver.BATCH_FILE, "a+") as output:
        for epi in episodes:
            output.write(f"{epi.episode_link}\n")


def download_tver(simulate=False) -> None:

    with open(Tver.BATCH_FILE, "r+") as input:
        links = input.readlines()
        
    if not links:
        Logger.warn(Messages.WARN_NO_VALID_LINKS)
        exit_script()

    ydl_opts = {
        "simulate": simulate,
        "writesubtitles": True,
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        Logger.info(Messages.PROCESS_DOWNLOAD)
        ydl.download(links)


if __name__ == "__main__":

    Logger.info(Messages.SCRIPT_START)

    reset_batch()

    if len(sys.argv) < 2:
        Logger.info(Messages.USAGE)
        exit_script()

    links = validate_links(sys.argv[1:])

    if not links.episodes and not links.series:
        Logger.warn(Messages.WARN_NO_VALID_LINKS)
        exit_script()

    if links.episodes:
        with Driver(), open(Tver.BATCH_FILE, "a+") as output:
            for episode in links.episodes:
                Logger.info(Messages.PROCESS_EPISODE % episode)
                
                if render_tver_episode(episode):
                    output.write(f"{episode}\n")
                    Logger.info(Messages.PROCESS_EPISODE_COMPLETE)

    if links.series:
        with Driver():
            for series in links.series:
                Logger.info(Messages.PROCESS_SERIES % series)

                if render_tver_series(series):
                    scrape_tver()

    download_tver()

    Logger.info(Messages.SCRIPT_COMPLETE)
