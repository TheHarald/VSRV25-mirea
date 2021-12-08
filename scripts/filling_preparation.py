from production_functions import *
from transport_functions import *
from routes import *
while True:
    find_and_move(fat_oven, filling_preparation, 'melted_fat', 2)
    join_ingredients(filling_preparation, ['boiled_milk', 'melted_fat'], 'filling', 2, 2)
