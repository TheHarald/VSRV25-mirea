start wt ' python delivery_in_storage.py ; sp -H -s 0.75 python move_from_storage.py ; sp -H -s 0.66 python cacao_furnace.py ; sp -H python dough.py '
start wt ' python cacao_oven.py ; sp -H -s 0.75 python candies.py ; sp -H -s 0.66 python chocolate_bar.py ; sp -H python chocolate_forming.py '
start wt ' python chocolate_mass.py ; sp -H -s 0.75 python fat_oven.py ; sp -H -s 0.66 python filling.py ; sp -H python filling_preparation.py '
start wt ' python fridge.py ; sp -H -s 0.8 python furnace.py ; sp -H -s 0.75 python packing_machine.py ; sp -H -s 0.66 python slicing.py ; sp -H python whipping_chocolate.py '
