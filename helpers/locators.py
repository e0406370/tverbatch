from helpers.constants import ClassNames
from helpers.utils import css_selector_class_starts_with, css_selector_class_contains_button
from selenium.webdriver.common.by import By

Locator = tuple[By, str]


class Locators:

    ERROR_MODAL: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.ERROR_MODAL),
    )

    TERMS_MODAL: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_contains_button(ClassNames.TERMS_MODAL)
    )

    LOAD_ICON: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.LOAD_ICON),
    )

    FILTER_LIST: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.FILTER_LIST),
    )
    
    FILTER_BUTTON: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_contains_button(ClassNames.FILTER_BUTTON),
    )

    SERIES_TITLE: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.SERIES_TITLE),
    )

    SERIES_DESCRIPTION: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.SERIES_DESCRIPTION),
    )

    EPISODE_LIST_EMPTY: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_LIST_EMPTY),
    )

    EPISODE_LIST: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_LIST),
    )

    EPISODE_ROW: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW),
    )

    EPISODE_ROW_TITLE: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW_TITLE),
    )

    EPISODE_ROW_BROADCAST_DATE: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW_BROADCAST_DATE),
    )

    EPISODE_ROW_END_DATE: Locator = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW_END_DATE),
    )
