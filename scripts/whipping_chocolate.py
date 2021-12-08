from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(chocolate_mass, whipping_chocolate, 'chocolate_mass', 1)
    join_ingredients(whipping_chocolate, ['chocolate_mass'], 'whipped_chocolate_mass', 1, 1)
