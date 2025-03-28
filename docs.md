# `anilibria` Documentation

## Installation
**Python 3.9 and higher required**

Ensure you have the required dependencies installed before using the library:

```
$ pip install m3u8-To-MP4
$ pip install requests
```

## Usage

Import the client and use its methods:

```py
from anilibria import AniLibriaClient

client = AniLibriaClient()
```

## Methods

### `search(title: str, filter: SearchFilter = SearchFilter()) -> list[Anime]`

Searches for anime titles based on the given title and optional filters.

**Parameters:**

`title` (str): The anime title to search for.

`filter` (SearchFilter, optional): Filters for refining the search.

**Returns:**

`list[Anime]`: A list of matching anime objects.

### `search_id(anime_id: int) -> Anime`

Retrieves information about an anime title using its ID.

**Parameters:**

`anime_id` (int): The unique ID of the anime.

**Returns:**

`Anime`: The anime object with details.

### `search_code(anime_code: str) -> Anime`

Fetches anime information using a unique code.

**Parameters:**

`anime_code` (str): The anime's code.

**Returns:**

`Anime`: The anime object with details.

### `all_years() -> List[int]`

Returns a list of all available release years for anime titles.

**Returns:**

`List[int]`: A sorted list of years.

### `all_genres() -> List[str]`

Returns a list of all anime genres sorted alphabetically.

**Returns:**

`List[str]`: A sorted list of genre names.

### `random() -> Anime`

Fetches a random anime title from the database.

**Returns:**

`Anime`: A randomly selected anime object.

### `updates(filter: UpdatesFilter = UpdatesFilter()) -> List[Anime]`

Retrieves a list of anime sorted by the latest release updates.

**Parameters:**

`filter (UpdatesFilter, optional)`: Filters for refining update results.

**Returns:**

`List[Anime]`: A list of recently updated anime objects.

### `schedule(day: int) -> List[Anime]`

Retrieves the anime schedule for a specific day of the week.

**Parameters:**

`day` (int): The day of the week (0 for Monday, 6 for Sunday).

**Returns:**

`List[Anime]`: A list of anime scheduled for the given day.

### `download(url: str, filename: str = None) -> None`

Downloads an anime episode from a given URL.

**Parameters:**

`url` (str): The URL of the episode to download.

`filename` (str, optional): The name of the output file.

### `async_download(url: str, filename: str = None) -> None`

Asynchronously downloads an anime episode from a given URL.

**Parameters:**

`url` (str): The URL of the episode to download.

`filename` (str, optional): The name of the output file.

