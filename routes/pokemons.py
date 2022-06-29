from hashlib import new
from types import new_class
from fastapi import APIRouter
from config.db import conn
from schemas.pokemons import pokemonEntity, pokemonsEntity
from models.pokemon import Pokemon


pokemon = APIRouter()

#find al pokemons
@pokemon.get('/pokemons')
def get_pokemon():
    return pokemonsEntity(conn.local.pokemon.find())
#create a pokemon
@pokemon.post('/pokemons')
def post_pokemon(pokemon:Pokemon):
    new_pokemon = dict(pokemon)
    del new_pokemon["id"]
    #connectig to database and creating a pokemon
    id = conn.local.pokemon.insert_one(new_pokemon).inserted_id

    pokemon = conn.local.pokemon.find_one({"_id": id})
    return pokemonEntity(pokemon)

    #return id assigned by mongoDB
    return str(id)


    
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