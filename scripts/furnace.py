from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(dough, furnace, 'dough', 2)
    join_ingredients(furnace, ['dough'], 'wffels', 2, 1)
