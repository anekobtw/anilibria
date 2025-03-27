from anilibria.client import AniLibriaClient

client = AniLibriaClient()
print(client.get_random().franchise_id)
