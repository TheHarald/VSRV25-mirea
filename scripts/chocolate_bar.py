from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(chocolate_mass, chocolate_bar, 'chocolate_mass', 1)
    join_ingredients(chocolate_bar, ['chocolate_mass'], 'chocolate_bar', 1, 1)
