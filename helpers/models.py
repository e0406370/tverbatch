class Links:
    def __init__(self, episodes: list[str], series: list[str]):
        self.episodes = episodes
        self.series = series
        
    def get_all(self) -> list[str]:
        return [*self.episodes, *self.series]


class Episode:
    def __init__(self, episode_link: str, episode_broadcast_date: str, episode_title: str):
        self.episode_link = episode_link
        self.episode_broadcast_date = episode_broadcast_date
        self.episode_title = episode_title

    def __str__(self):
        parts = [self.episode_link]

        if self.episode_broadcast_date:
            parts.append(self.episode_broadcast_date)

        if self.episode_title:
            parts.append(self.episode_title)

        return " | ".join(parts)
