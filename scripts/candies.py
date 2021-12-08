from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(chocolate_mass, candies, 'chocolate_mass', 1)
    join_ingredients(candies, ['chocolate_mass'], 'candies', 1, 1)
