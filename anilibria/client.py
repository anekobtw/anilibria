from typing import List

import m3u8_To_MP4

from anilibria.models import Anime, SearchFilter, UpdatesFilter
from anilibria.rest_adapter import RestAdapter


class AniLibriaClient:
    def __init__(self) -> None:
        self._rest_adapter = RestAdapter()

    def search(self, title: str, filter: SearchFilter = SearchFilter()) -> list[Anime]:
        """Возвращает список найденных по фильтрам тайтлов"""
        response = self._rest_adapter.get(f"/title/search?search={title}" + str(filter))
        return [Anime(anime) for anime in response["list"]]

    def search_id(self, anime_id: int) -> Anime:
        """Получить информацию о тайтле по его айди"""
        return Anime(self._rest_adapter.get(f"/title?id={anime_id}"))

    def search_code(self, anime_code: str) -> Anime:
        """Получить информацию о тайтле по его коду"""
        return Anime(self._rest_adapter.get(f"/title?code={anime_code}"))

    def all_years(self) -> List[int]:
        """Возвращает список годов выхода доступных тайтлов по возрастанию"""
        return self._rest_adapter.get("/years")

    def all_genres(self) -> List[str]:
        """Возвращает список всех жанров по алфавиту"""
        return self._rest_adapter.get("/genres")

    def random(self) -> Anime:
        """Возвращает случайный тайтл из базы"""
        return Anime(self._rest_adapter.get("/title/random"))

    def updates(self, filter: UpdatesFilter = UpdatesFilter()) -> List[Anime]:
        """Список тайтлов, отсортированные по времени добавления нового релиза."""
        animes = self._rest_adapter.get(f"/title/updates?{filter}")
        return [Anime(anime) for anime in animes.get("list")]

    def schedule(self, day: int) -> List[Anime]:
        """Расписание выхода тайтлов, отсортированное по дням недели"""
        animes = self._rest_adapter.get(f"/title/schedule?days={day}")
        return [Anime(anime) for anime in animes[0].get("list")]

    def download(self, url: str, filename: str = None) -> None:
        """Скачивает эпизод по ссылке"""
        if filename:
            m3u8_To_MP4.multithread_download(m3u8_uri=url, mp4_file_name=filename)
        else:
            m3u8_To_MP4.multithread_download(m3u8_uri=url)

    def async_download(self, url: str, filename: str = None) -> None:
        """Асинхронно скачивает эпизод по ссылке"""
        if filename:
            m3u8_To_MP4.async_download(m3u8_uri=url, mp4_file_name=filename)
        else:
            m3u8_To_MP4.async_download(m3u8_uri=url)
