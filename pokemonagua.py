import requests
from typing import List, Optional, Dict, Any

def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching data from {url}: {e}")
        return None
    pass 

def get_water_type_url() -> Optional[str]:
    url = "https://pokeapi.co/api/v2/type/"
    data = fetch_data(url)
    if data:
        for pokemon_type in data.get("results", []):
            if pokemon_type.get("name") == "water":
                return pokemon_type.get("url")
            
            """ Esta funcion entra en la que aparecen los tipos con sus respectivas urls y
            te devuelve la que tiene el name water que es: https://pokeapi.co/api/v2/type/11/"""
            
    return None
    pass

def fetch_water_pokemons() -> List[str]:
    water_type_url = get_water_type_url()
    if not water_type_url:
        return []
    data = fetch_data(water_type_url)
    if data:
        return [pokemon.get("pokemon", {}).get("name") for pokemon in data.get("pokemon", []) if pokemon.get("pokemon")]
    return []
    pass

def display_pokemons(pokemons: List[str]) -> None:
    if pokemons:
        print("List of Water-type Pokémon:")
        for name in pokemons:
            print(f"- {name}")
    else:
        print("No Water-type Pokémon found.")
    pass

if __name__ == "__main__":
    water_pokemons = fetch_water_pokemons()
    display_pokemons(water_pokemons)
    pass

