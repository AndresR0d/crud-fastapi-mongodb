from fastapi import APIRouter
from config.db import conn
from schemas.pokemons import pokemonEntity, pokemonsEntity


pokemon = APIRouter()

#find al pokemons
@pokemon.get('/pokemons')
def get_pokemon():
    return pokemonsEntity(conn.local.pokemon.find())
#create a pokemon
@pokemon.post('/pokemons')
def post_pokemon():
    return "hello world"
#get pokemon by id (pokedex number)
@pokemon.get('/pokemons/{id}')
def get_pokemon_by_id():
    return "hello world"
#modify pokemon
@pokemon.put('/pokemons/{id}')
def update_pokemon():
    return "hello world"
#remove pokemon
@pokemon.delete('/pokemons')
def delete_pokemon():
    return "hello world"