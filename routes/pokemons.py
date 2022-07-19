from types import new_class
from fastapi import APIRouter, Response
from config.db import conn
from schemas.pokemons import pokemonEntity, pokemonsEntity
from models.pokemon import Pokemon
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT



pokemon = APIRouter()

#find all pokemons
@pokemon.get('/pokemons')
def find_all_pokemons():
    return pokemonsEntity(conn.local.pokemon.find())
#create a pokemon
@pokemon.post('/pokemons/')
def post_pokemon(pokemon:Pokemon):
    new_pokemon = dict(pokemon)
    del new_pokemon["id"]
    #connectig to database and creating a pokemon
    id = conn.local.pokemon.insert_one(new_pokemon).inserted_id

    pokemon = conn.local.pokemon.find_one({"_id": id})
    return pokemonEntity(pokemon)

    #return id assigned by mongoDB
    #return str(id)

#get pokemon by id (pokedex number)
@pokemon.get('/pokemons/{dex_num}')
def get_pokemon_by_id(dex_num: int):
    #Query to get pokemon by id (id is dex_num)
    return pokemonEntity(conn.local.pokemon.find_one({"dex_num": dex_num}))
    
#modify pokemon
@pokemon.put('/pokemons/{id}')
def update_pokemon():
    return "hello world"
#remove pokemon
@pokemon.delete('/pokemons/{id}')
def delete_pokemon(id:str):
    pokemonEntity(conn.local.pokemon.find_one_and_delete({{"_id":ObjectId(id)}}))
    return Response(status_code=HTTP_204_NO_CONTENT)
