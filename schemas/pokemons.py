def pokemonEntity(item) -> dict:
    return{
        "id":item["id"],
        "dex_num":["dex_num"],
        "name":item["name"],
        "type1":item["type1"],
        "type2": item["type2"]
    }

def pokemonsEntity(entity) -> list:
    [pokemonEntity(item) for item in entity]
