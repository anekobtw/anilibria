from typing import List

import m3u8_To_MP4
import requests

from anilibria.exceptions import SearchException
from anilibria.models import Anime, Filter


class AniLibriaClient:
    BASE_URL = "https://api.anilibria.tv/v3/"

    def search(self, title: str, filter: Filter) -> list[Anime]:
        response = requests.get(self.BASE_URL + f"title/search?search={title}" + str(filter)).json()
        return [Anime(anime) for anime in response["list"]]

    def search_id(self, anime_id: int) -> Anime:
        response = requests.get(self.BASE_URL + f"title?id={anime_id}").json()
        if "error" in response:
            raise SearchException(response["error"]["message"])
        return Anime(response)

    def search_code(self, anime_code: str) -> Anime:
        response = requests.get(self.BASE_URL + f"title?code={anime_code}").json()
        if "error" in response:
            raise SearchException(response["error"]["message"])
        return Anime(response)

    def get_random(self) -> Anime:
        response = requests.get(self.BASE_URL + f"title/random").json()
        return Anime(response)

    def all_years(self) -> List[int]:
        response = requests.get(self.BASE_URL + "years").json()
        return response

    def all_genres(self) -> List[str]:
        response = requests.get(self.BASE_URL + "genres").json()
        return response

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
