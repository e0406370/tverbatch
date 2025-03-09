## Overview

This command-line tool retrieves episode links from one or more series currently streaming on [TVer](https://tver.jp/) and saves them to a text file, using **Selenium** and **Beautiful Soup**. Afterwards, it executes **yt-dlp** internally to download the episodes.

## Requirements

Note: This script requires at least <ins>**Python 3.9**<ins>.

Assuming the CLI is in the **`tverbatch`** directory, install all required dependencies by running:

```sh
pip install -r requirements.txt
```

## **Usage**

Assuming the CLI is in the **`tverbatch`** directory, execute the following command:

```sh
python tver.py [-f] URL [URL...]
```

`URL` can be one of the following formats:
- `episode_url => https://tver.jp/episodes/ep12345678`
- `episode_id => ep12345678`
- `series_url => https://tver.jp/series/sr12345678`
- `series_id => sr12345678`

The `-f` flag enables filtering of episodes based on the categories shown on the series page.
If this flag is not provided, the script will attempt to download all available episodes by default.

The episodes will be downloaded to the **`downloads`** folder, with subtitles included where available.
