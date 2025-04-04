from dataclasses import dataclass, field
from typing import ClassVar, Dict, List, Optional, Union


@dataclass
class Episode:
    """Represents an anime episode with metadata and streaming URLs."""

    data: Optional[dict] = None

    episode: Optional[int] = None
    name: Optional[str] = None
    created_timestamp: Optional[int] = None
    preview: str = ""
    opening: List[int] = field(default_factory=list)
    ending: List[int] = field(default_factory=list)
    fhd_url: Optional[str] = None
    hd_url: Optional[str] = None
    sd_url: Optional[str] = None

    BASE_HOST: ClassVar[str] = "https://cache.libria.fun"

    def __post_init__(self) -> None:
        if isinstance(self.data, dict):
            self.episode = self.data.get("episode")
            self.name = self.data.get("name")
            self.created_timestamp = self.data.get("created_timestamp")
            self.preview = self.data.get("preview", "")

            skips = self.data.get("skips", {})
            self.opening = skips.get("opening", [])
            self.ending = skips.get("ending", [])

            hls = self.data.get("hls", {})
            self.fhd_url = f"{self.BASE_HOST}{hls.get('fhd', '')}" if hls.get("fhd") else None
            self.hd_url = f"{self.BASE_HOST}{hls.get('hd', '')}" if hls.get("hd") else None
            self.sd_url = f"{self.BASE_HOST}{hls.get('sd', '')}" if hls.get("sd") else None


@dataclass
class Anime:
    """Represents an anime with detailed metadata and episodes."""

    data: Optional[dict] = None

    id: int = 0
    code: str = ""
    name_ru: Optional[str] = None
    name_en: Optional[str] = None
    name_alternative: Optional[str] = None
    franchise_id: Optional[str] = None
    status: Optional[str] = None
    status_code: Optional[int] = None
    poster_small_url: str = ""
    poster_medium_url: str = ""
    poster_original_url: str = ""
    updated: int = 0
    last_change: int = 0
    type: Optional[str] = None
    type_short: Optional[str] = None
    episodes_count: int = 0
    episode_length: int = 0
    genres: List[str] = field(default_factory=list)
    team: Dict[str, List] = field(default_factory=dict)
    description: str = ""
    in_favorites: int = 0
    is_blocked: bool = False
    season: Optional[str] = None
    year: Optional[int] = None
    episodes: List[Episode] = field(default_factory=list)

    BASE_HOST = "https://anilibria.top"

    def __post_init__(self) -> None:
        # If initialized from dict (backward compatibility)
        if isinstance(self.data, dict):
            self.id = self.data.get("id", 0)
            self.code = self.data.get("code", "")

            names = self.data.get("names", {})
            self.name_ru = names.get("ru")
            self.name_en = names.get("en")
            self.name_alternative = names.get("alternative")

            franchises = self.data.get("franchises", [])
            if franchises:
                self.franchise_id = franchises[0].get("franchise", {}).get("id", None)

            status = self.data.get("status", {})
            self.status = status.get("string")
            self.status_code = status.get("code")

            posters = self.data.get("posters", {})
            self.poster_small_url = self.BASE_HOST + posters.get("small", {}).get("url", "")
            self.poster_medium_url = self.BASE_HOST + posters.get("medium", {}).get("url", "")
            self.poster_original_url = self.BASE_HOST + posters.get("original", {}).get("url", "")

            self.updated = self.data.get("updated", 0)
            self.last_change = self.data.get("last_change", 0)

            anime_type = self.data.get("type", {})
            self.type = anime_type.get("full_string")
            self.type_short = anime_type.get("string")
            self.episodes_count = anime_type.get("episodes", 0)
            self.episode_length = anime_type.get("length", 0)

            self.genres = self.data.get("genres", [])
            self.team = self.data.get("team", {})
            self.description = self.data.get("description", "")
            self.in_favorites = self.data.get("in_favorites", 0)
            self.is_blocked = self.data.get("blocked", {}).get("blocked", False)

            season = self.data.get("season", {})
            self.season = season.get("string")
            self.year = season.get("year")

            self.episodes = [
                            Episode(ep)
                            for ep in (
                                self.data.get("player", {}).get("list", {})
                                if isinstance(self.data.get("player", {}).get("list", {}), list)
                                else self.data.get("player", {}).get("list", {}).values()
                            )
                        ]

class Filter:
    def get_params(self) -> Dict[str, List[str]]:
        return {}

    def __str__(self) -> str:
        params = []
        for key, value in self.get_params().items():
            if value:
                params.append(f"{key}={value}")
        return "&".join(params) if params else ""


@dataclass
class SearchFilter(Filter):
    years: List[int] = field(default_factory=list)
    types: List[str] = field(default_factory=list)
    seasons: List[str] = field(default_factory=list)
    genres: List[str] = field(default_factory=list)
    page: int = None
    limit: int = None

    def get_params(self) -> Dict[str, List[Union[int, str]]]:
        params = {}
        params["year"] = ",".join(map(str, self.years))
        params["types"] = ",".join(self.types)
        params["seasons"] = ",".join(self.seasons)
        params["genres"] = ",".join(self.genres)
        params["page"] = self.page
        params["limit"] = self.limit
        return params


@dataclass
class UpdatesFilter(Filter):
    limit: Optional[int] = None
    since: Optional[int] = None
    page: Optional[int] = None
    items_per_page: Optional[int] = None

    def get_params(self) -> Dict[str, List[Union[int, str]]]:
        params = {}
        params["limit"] = self.limit
        params["since"] = self.since
        params["page"] = self.page
        params["items_per_page"] = self.items_per_page
        return params
