# AniLibriaClient Documentation

# Quick Links
- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
  - [search()](#searchtitle-str-filter-searchfilter--searchfilter---listanime)
  - [search_id()](#search_idanime_id-int---anime)
  - [search_code()](#search_codeanime_code-str---anime)
  - [all_years()](#all_years---listint)
  - [all_genres()](#all_genres---liststr)
  - [random()](#random---anime)
  - [updates()](#updatesfilter-updatesfilter--updatesfilter---listanime)
  - [schedule()](#scheduleday-int---listanime)
  - [download()](#downloadurl-str-filename-str--none---none)
  - [async_download()](#async_downloadurl-str-filename-str--none---none)
- [Data Models](#data-models)
  - [Anime](#anime)
  - [Episode](#episode)
  - [SearchFilter](#searchfilter)
  - [UpdatesFilter](#updatesfilter)

## Installation
**Python 3.9 and higher required**

Ensure you have the required dependencies installed before using AniLibriaClient:
```bash
pip install anilibria
```

## Usage
Import the client and use its methods:
```python
from anilibria import AniLibriaClient

client = AniLibriaClient()
```

## Methods

### `search(title: str, filter: SearchFilter = SearchFilter()) -> list[Anime]`
Searches for anime titles based on the given `title` and optional filters.

**Parameters:**
- `title` (str): The anime title to search for.
- `filter` (SearchFilter, optional): Filters for refining the search.

**Returns:**
- `list[Anime]`: A list of matching anime objects.

```python
results = client.search("Тетрадь смерти")
for anime in results:
    print(anime.name_ru)
```

### `search_id(anime_id: int) -> Anime`
Retrieves information about an anime title using its ID.

**Parameters:**
- `anime_id` (int): The unique ID of the anime.

**Returns:**
- `Anime`: The anime object with details.

```python
anime = client.search_id(5158)
print(anime.name_ru)
```

### `search_code(anime_code: str) -> Anime`
Fetches anime information using a unique code.

**Parameters:**
- `anime_code` (str): The anime's code.

**Returns:**
- `Anime`: The anime object with details.

```python
anime = client.search_code("death-note-netflix")
print(anime.name_ru)
```

### `all_years() -> List[int]`
Returns a list of all available release years for anime titles.

**Returns:**
- `List[int]`: A sorted list of years.

```python
years = client.all_years()
print(years)  # [1995, 1996, 1998, 1999, 2001, 2003, 2004, 2005, 2006, ...]
```

### `all_genres() -> List[str]`
Returns a list of all anime genres sorted alphabetically.

**Returns:**
- `List[str]`: A sorted list of genre names.

```python
genres = client.all_genres()
print(genres)  # ['Боевые искусства', 'Вампиры', 'Гарем', 'Демоны', ...]
```

### `random() -> Anime`
Fetches a random anime from the database.

**Returns:**
- `Anime`: A randomly selected anime object.

```python
random_anime = client.random()
print(random_anime.name_ru)
```

### `updates(filter: UpdatesFilter = UpdatesFilter()) -> List[Anime]`
Retrieves a list of anime sorted by the latest release updates.

**Parameters:**
- `filter` (UpdatesFilter, optional): Filters for refining update results.

**Returns:**
- `List[Anime]`: A list of recently updated anime objects.

```python
updates = client.updates()
for anime in updates:
    print(anime.name_ru)
```

### `schedule(day: int) -> List[Anime]`
Retrieves the anime schedule for a specific day of the week.

**Parameters:**
- `day` (int): The day of the week (0 for Monday, 6 for Sunday).

**Returns:**
- `List[Anime]`: A list of anime scheduled for the given day.

```python
monday_schedule = client.schedule(1)
for anime in monday_schedule:
    print(anime.name_ru)
```

### `download(url: str, filename: str = None) -> None`
Downloads an anime episode from a given URL.

**Parameters:**
- `url` (str): The URL of the episode to download.
- `filename` (str, optional): The name of the output file.

```python
client.download(anime.episodes[0].fhd_url, "episode.mp4")
```

### `async_download(url: str, filename: str = None) -> None`
Asynchronously downloads an anime episode from a given URL.

**Parameters:**
- `url` (str): The URL of the episode to download.
- `filename` (str, optional): The name of the output file.

```python
client.async_download(anime.episodes[0].fhd_url, "episode.mp4")
```

## Data Models

### `Anime`
Represents an anime with detailed metadata and episodes.

**Attributes:**
- `id` (int): The unique ID of the anime.
- `code` (str): The unique code of the anime.
- `name_ru` (Optional[str]): The Russian title of the anime.
- `name_en` (Optional[str]): The English title of the anime.
- `name_alternative` (Optional[str]): Alternative title of the anime.
- `franchise_id` (Optional[str]): The franchise ID the anime belongs to.
- `status` (Optional[str]): The release status of the anime.
- `status_code` (Optional[int]): The status code representing the anime's availability.
- `poster_small_url`, `poster_medium_url`, `poster_original_url` (str): URLs for different sizes of the anime poster.
- `updated` (int): Timestamp of the last update.
- `last_change` (int): Timestamp of the last change.
- `type` (Optional[str]): The full type description (e.g., "TV Series").
- `type_short` (Optional[str]): The short type description (e.g., "TV").
- `episodes_count` (int): The total number of episodes.
- `episode_length` (int): The average length of an episode in minutes.
- `genres` (List[str]): The list of genres.
- `team` (Dict[str, List]): Information about the anime's production team.
- `description` (str): The synopsis of the anime.
- `in_favorites` (int): Number of users who have favorited the anime.
- `is_blocked` (bool): Whether the anime is blocked.
- `season` (Optional[str]): The season in which the anime aired.
- `year` (Optional[int]): The release year.
- `episodes` (List[Episode]): A list of available episodes.

### `Episode`
Represents an anime episode with metadata and streaming URLs.

**Attributes:**
- `episode` (Optional[int]): The episode number.
- `name` (Optional[str]): The episode title.
- `created_timestamp` (Optional[int]): The timestamp of when the episode was added.
- `preview` (str): URL to the episode preview image.
- `opening` (List[int]): List of timestamps for the opening.
- `ending` (List[int]): List of timestamps for the ending.
- `fhd_url`, `hd_url`, `sd_url` (Optional[str]): URLs for different quality versions of the episode.

### `SearchFilter`
Filter class for refining anime searches.

**Attributes:**
- `years` (List[int]): List of years to filter results by.
- `types` (List[str]): List of anime types (e.g., TV, OVA, Movie).
- `seasons` (List[str]): List of seasons (e.g., Winter, Spring).
- `genres` (List[str]): List of genres to filter by.
- `page` (int): The page number of the search results.

### `UpdatesFilter`
Filter class for retrieving anime updates.

**Attributes:**
- `limit` (Optional[int]): The maximum number of results to return.
- `since` (Optional[int]): Timestamp for filtering updates from a certain point in time.
- `page` (Optional[int]): The page number of update results.
- `items_per_page` (Optional[int]): Number of items per page.
