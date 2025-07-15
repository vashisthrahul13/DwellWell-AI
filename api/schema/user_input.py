from pydantic import BaseModel,Field
from typing import Annotated,Literal

#create input class
class UserInput(BaseModel):
    sector : Annotated[str,Field(...,description='Sector in which the house is located',example = 'sector 39')]

    super_area : Annotated [float,Field(...,description='Super built up area in sqft',gt=100.0,lt=10000.0, example = 1247.5)]

    bedrooms : Annotated[int,Field(...,description='Number of bedrooms in the house',ge=1,lt=6, example = 2)]

    bathroom : Annotated[int,Field(...,description='Number of bathrooms in the house',ge=1,lt=7, example = 2)]

    balcony :Annotated[str,Field(...,description='Number of balcony in the house',example = '2')]

    age_possession : Annotated[str,Field(...,description='How old is the house',example = '0 to 1 year old')]

    servant_room :Annotated[bool,Field(...,description='Does the house have a servant room',example = 'Yes')]

    luxury_category :Annotated[Literal['low','medium','high'],Field(...,description='How luxurious is the housing project',example = 'High')]

    parking :Annotated[int,Field(...,description='Number of alloted parking spaces',example = 2)]
    
    building_type : Annotated[str,Field(...,description='How tall is the building',example = 'High-rise')]


