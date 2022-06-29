from lib2to3.pytree import Base
from typing import Optional
from pydantic import BaseModel

class Pokemon(BaseModel):
    id : Optional[str]
    dex_num : int
    name : str
    type1 : str
    type2 : Optional[str] 
    
