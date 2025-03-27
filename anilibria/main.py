from typing import Dict, List

import m3u8_To_MP4
import requests


class Episode:
    """Represents an anime episode with metadata and streaming URLs."""

    BASE_HOST = "https://cache.libria.fun"

    def __init__(self, data: Dict) -> None:
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict, got {type(data).__name__}: {data}")

        self.episode: int = data.get("episode", None)
        self.name: str = data.get("name", None)
        self.created_timestamp: int = data.get("created_timestamp", None)
        self.preview: str = data.get("preview", "")

        self.opening: List[int] = data.get("skips", {}).get("opening", [])
        self.ending: List[int] = data.get("skips", {}).get("ending", [])

        hls = data.get("hls", {})
        fhd = hls.get("fhd", "")
        hd = hls.get("hd", "")
        sd = hls.get("sd", "")
        self.fhd_url: str = f"{self.BASE_HOST}{fhd}" if fhd else None
        self.hd_url: str = f"{self.BASE_HOST}{hd}" if hd else None
        self.sd_url: str = f"{self.BASE_HOST}{sd}" if sd else None


class Anime:
    """Represents an anime with detailed metadata and episodes."""

    def __init__(self, data: Dict) -> None:
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict, got {type(data).__name__}: {data}")

        self.id: int = data.get("id", 0)
        self.code: str = data.get("code", "")
        self.name_ru: str = data.get("names", {}).get("ru", None)
        self.name_en: str = data.get("names", {}).get("en", None)
        self.name_alternative: str = data.get("names", {}).get("alternative", None)

        self.status: str = data.get("status", {}).get("string", None)
        self.status_code: int = data.get("status", {}).get("code", None)

        posters = data.get("posters", {})
        self.poster_small_url: str = posters.get("small", {}).get("url", "")
        self.poster_medium_url: str = posters.get("medium", {}).get("url", "")
        self.poster_original_url: str = posters.get("original", {}).get("url", "")

        self.updated: int = data.get("updated", 0)
        self.last_change: int = data.get("last_change", 0)

        anime_type = data.get("type", {})
        self.type: str = anime_type.get("full_string", None)
        self.type_short: str = anime_type.get("string", None)
        self.episodes_count: int = anime_type.get("episodes", 0)
        self.episode_length: int = anime_type.get("length", 0)

        self.genres: List[str] = data.get("genres", [])
        self.team: Dict[str, List] = data.get("team", {})
        self.description: str = data.get("description", "")
        self.in_favorites: int = data.get("in_favorites", 0)
        self.is_blocked: bool = data.get("blocked", {}).get("blocked", False)

        self.season: str = data.get("season", {}).get("string", None)
        self.year: int = data.get("season", {}).get("year", None)

        self.episodes: List[Episode] = [Episode(ep) for ep in data.get("player", {}).get("list", []).values()]


class AniLibriaClient:
    BASE_URL = "https://api.anilibria.tv/v3/"

    def search(self, title: str) -> list[Anime]:
        response = requests.get(self.BASE_URL + f"title/search?search={title}").json()
        return [Anime(anime) for anime in response["list"]]

    def search_id(self, anime_id: int) -> Anime:
        response = requests.get(self.BASE_URL + f"title?id={anime_id}").json()
        if "error" in response:
            raise Exception(response["error"]["message"])
        return Anime(response)

    def search_code(self, anime_code: str) -> Anime:
        response = requests.get(self.BASE_URL + f"title?code={anime_code}").json()
        if "error" in response:
            raise Exception(response["error"]["message"])
        return Anime(response)

    def download(self, url: str, filename: str = None) -> None:
        if filename:
            m3u8_To_MP4.multithread_download(m3u8_uri=url, mp4_file_name=filename)
        else:
            m3u8_To_MP4.multithread_download(m3u8_uri=url)

    def async_download(self, url: str, filename: str = None) -> None:
        if filename:
            m3u8_To_MP4.async_download(m3u8_uri=url, mp4_file_name=filename)
        else:
            m3u8_To_MP4.async_download(m3u8_uri=url)


if __name__ == "__main__":
    client = AniLibriaClient()
    anime = client.search("рон камонохаши")[0]
    print(client.search_code(anime.code).genres)
