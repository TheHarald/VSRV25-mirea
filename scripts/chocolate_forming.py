from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(slicing, chocolate_forming, 'sliced_waffles', 2)
    find_and_move(whipping_chocolate, chocolate_forming, 'whipped_chocolate_mass', 2)
    join_ingredients(chocolate_forming, [
        'sliced_waffles',
        'whipped_chocolate_mass'
    ], 'chocolate_waffles', 2, 1)
