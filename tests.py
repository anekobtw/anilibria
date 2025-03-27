import logging

from anilibria.client import AniLibriaClient

# forcing because urllib3 has a warning level
logging.basicConfig(force=True, level=logging.DEBUG, format="%(asctime)s | %(name)s | %(message)s")

client = AniLibriaClient()
anime = client.get_random()
print(f"Название рандомного аниме: {anime.name_ru}")
