"""
Jesteśmy w pokoju z pokemonami, i mamy wielką walizkę, w której
możemy unieść 2000 wagi.
Program spyta nas, czy chcemy wziąć kolejnego pokemona do walizki.
Jeśli powiemy "tak", to poinformuje nas ile miejsca w walizce nam zostało.
Jeśli powiemy "tak" i skończy nam się miejsce w walizce - PRZEGRYWAMY.
Jeśli powiemy "nie", gra się kończy i printuje pokemony, które
zabieramy ze sobą do domu ^_^
"""

import httpx
import random
from dataclasses import dataclass


# class Pokemon:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight


@dataclass
class Pokemon:
    name: str
    weight: int


def get_random_pokemon():
    pokemon_id = random.randint(1, 151)
    response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    pokemon_data = response.json()
    return Pokemon(pokemon_data["name"], pokemon_data["weight"])


def main():
    pokemon = get_random_pokemon()
    suitcase = pokemon.weight
    pokemons_in_suitcase = [pokemon.name]
    print(f"You found {pokemon.name}! Suitcase load: {suitcase}/2000")
    while input("Do you want to take another Pokemon with you? (y/n): ") == "y":
        pokemon = get_random_pokemon()
        suitcase += pokemon.weight
        pokemons_in_suitcase.append(pokemon.name)
        if suitcase > 2000:
            print(f"You found {pokemon.name} (weight {pokemon.weight})! Suitcase overloaded! You lost! :(")
            break
        print(f"You found {pokemon.name}! Suitcase load: {suitcase}/2000")
    else:
        print(f"Contrats, you took {', '.join(pokemons_in_suitcase)} with you :)")



if __name__ == '__main__':
    main()


