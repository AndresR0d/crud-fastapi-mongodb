from fastapi import FastAPI
from routes.pokemons import pokemon

app = FastAPI()

app.include_router(pokemon)
