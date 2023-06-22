import requests


API_URL = "https://pokeapi.co/api/v2/pokemon/"
limit = 100
def get_pokemon_list():
    response = requests.get(f"{API_URL}?limit={limit}")
    data = response.json()
    return data["results"]


def get_pokemon_details(url):
    response = requests.get(url)
    data = response.json()
    return data

def search_pokemon(pokemon_list, query):
    query = query.lower()
    for pokemon in pokemon_list:
        if query == pokemon["name"]:
            return pokemon
    return None