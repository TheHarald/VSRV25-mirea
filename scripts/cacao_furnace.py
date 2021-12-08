from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_ingredients(cocoa_oven, ['cocoa_butter'], 'melted_cocoa_butter', 2, 1)
    find_and_move(cocoa_oven, chocolate_mass, 'melted_cocoa_butter', 2)
