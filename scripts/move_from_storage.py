from transport_functions import *
from routes import *
while True:
    find_and_move(start_storage, cocoa_oven, 'cocoa_butter', 2)
    find_and_move(start_storage, chocolate_mass, 'sugar', 2)
    find_and_move(start_storage, fat_oven, 'confectionery_fat', 2)
    find_and_move(start_storage, filling_preparation, 'boiled_milk', 2)
    # тесто
    find_and_move(start_storage, dough, 'flour', 2)
    find_and_move(start_storage, dough, 'egg', 2)
    find_and_move(start_storage, dough, 'butter', 2)
    find_and_move(start_storage, dough, 'sugar', 2)
    find_and_move(start_storage, dough, 'milk', 2)
