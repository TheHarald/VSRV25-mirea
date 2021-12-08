from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(cocoa_oven, chocolate_mass, 'melted_cocoa_butter', 1)
    join_ingredients(chocolate_mass, ['melted_cocoa_butter'], 'chocolate_mass', 1, 1)
