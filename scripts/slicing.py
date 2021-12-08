from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(filling, slicing, 'waffle_bed', 2)
    join_ingredients(slicing, ['waffle_bed'], 'sliced_waffles', 2, 1)