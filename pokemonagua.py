import requests
from typing import List, Optional

def fetch_data(url: str) -> Optional[dict]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print(f"Error fetching data from {url}")
        return None

def get_water_pokemon() -> List[str]:
    type_url = "https://pokeapi.co/api/v2/type/water"
    data = fetch_data(type_url)
    return [pokemon["pokemon"]["name"] for pokemon in data["pokemon"]] if data else []

def display_pokemons(pokemons: List[str]) -> None:
    if pokemons:
        print("List of Water-type Pokémon:")
        for name in pokemons:
            print(f"- {name}")
    else:
        print("No Water-type Pokémon found.")

if __name__ == "__main__":
    water_pokemons = get_water_pokemon()
    display_pokemons(water_pokemons)

