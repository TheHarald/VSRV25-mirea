from production_functions import *
from transport_functions import *
from routes import *
while True:
    create_ingredients(waffels_package, 'package', 1, 1)
    find_and_move(waffles_fridge, waffels_package, 'chocolate_waffles', 2)
    join_ingredients(waffels_package,
                     ['chocolate_waffles', 'package'],
                     'packed_chocolate_waffles', 2, 2)
    find_and_move(waffels_package, end_storage, 'packed_chocolate_waffles', 2)

    create_ingredients(candies_package, 'package', 1, 1)
    find_and_move(candies_fridge, candies_package, 'candies', 2)
    join_ingredients(candies_package,
                     ['candies', 'package'],
                     'packed_candies', 2, 2)
    find_and_move(candies_package, end_storage, 'packed_candies', 2)

    create_ingredients(chocolate_package, 'package', 1, 1)
    find_and_move(chocolate_fridge, chocolate_package, 'chocolate_bar', 2)
    join_ingredients(chocolate_package,
                     ['chocolate_bar', 'package'],
                     'packed_chocolate', 2, 2)
    find_and_move(chocolate_package, end_storage, 'packed_chocolate', 2)
