from anilibria import AniLibriaClient, Anime
import logging

logging.basicConfig(force=True, level=logging.DEBUG)

client = AniLibriaClient()


# Searching
client.search("Тетрадь смерти")  # Это вернет список объектов типа "Anime"
client.search_id(5158)  # Также, Вы можете найти аниме, если у Вас есть его айди
client.search_code("death-note-netflix")  # Или код


# Get all genres/years
print(client.all_genres())
print(client.all_years())
