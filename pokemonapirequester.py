'''
10/12/26
'''

import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data of: {name}\nStatus code: {response.status_code}")
        return None


while True:
    pokemon_name = input("Pokemon name (q to quit): ").lower()

    if pokemon_name == "q":
        print("Goodbye!")
        break

    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"\nName: {pokemon_info['name'].capitalize()}")
        print(f"Id: {pokemon_info['id']}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")

        types = [t["type"]["name"].capitalize() for t in pokemon_info["types"]]
        print(f"Type: {', '.join(types)}\n")

        