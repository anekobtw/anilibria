from typing import List

import m3u8_To_MP4
import requests

from anilibria.models import Anime, Filter
from anilibria.rest_adapter import RestAdapter


class AniLibriaClient:
    def __init__(self) -> None:
        self._rest_adapter = RestAdapter()

    def search(self, title: str, filter: Filter = Filter()) -> list[Anime]:
        response = self._rest_adapter.get(f"/title/search?search={title}" + str(filter))
        return [Anime(anime) for anime in response["list"]]

    def search_id(self, anime_id: int) -> Anime:
        return Anime(self._rest_adapter.get(f"/title?id={anime_id}"))

    def search_code(self, anime_code: str) -> Anime:
        return Anime(self._rest_adapter.get(f"/title?code={anime_code}"))

    def get_random(self) -> Anime:
        return Anime(self._rest_adapter.get("/title/random"))

    def all_years(self) -> List[int]:
        return self._rest_adapter.get("/years")

    def all_genres(self) -> List[str]:
        return self._rest_adapter.get("/genres")

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
