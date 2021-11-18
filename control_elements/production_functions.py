import random
import time
from routes import *


# путь, имя продукта, вредя приготовления, количество.
def create_ingredients(path, name, time_for_cooking, count):
    time.sleep(time_for_cooking)
    for i in range(count):
        open(f'{path}{name}{random.randint(1, 1000)}_{i}', 'a').close()
        # print(name, i, 'created')


create_ingredients(start_storage, 'cake', 3, 5)
