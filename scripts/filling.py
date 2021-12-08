from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(filling_preparation, filling, 'filling', 2)
    find_and_move(furnace, filling, 'wffels', 2)
    join_ingredients(filling, ['wffels', 'filling'], 'waffle_bed', 2, 1)
