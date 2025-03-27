import logging

from anilibria.client import AniLibriaClient
from anilibria.models import SearchFilter, UpdatesFilter

logging.basicConfig(force=True, level=logging.DEBUG, format="%(levelname)s | %(asctime)s | %(name)s | %(message)s")

client = AniLibriaClient()
for anime in client.updates(filter=UpdatesFilter(page=None, limit=None)):
    print(anime.name_ru)
