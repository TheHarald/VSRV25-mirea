import random
import time
from routes import *
import os
import re


# путь, имя продукта, вредя приготовления, количество.
# создаёт игредиент в папке назанчения
def create_ingredients(path, name, time_for_cooking, count):
    time.sleep(time_for_cooking)
    for i in range(count):
        open(f'{path}{name}{random.randint(1, 1000)}_{i}', 'a').close()
    print(count, name, 'created')


# объеденить несколько ингредиентов в 1
def join_ingredients(path, ingredients, name, time_for_cooking, count):
    items = os.listdir(path)
    temp_ingredients = []
    # print('join', items)
    # print(path)
    # print(name)
    # print(time_for_cooking)
    # print(count)
    # print(ingredients)
    # print(re.match('red', items[0]))
    for ingredient in ingredients:
        for item in items:
            # print(re.match(ingredient, item))
            if re.match(ingredient, item):
                print('find', item)
                temp_ingredients.append(item)
                break

    if len(temp_ingredients) == len(ingredients):
        for temp_ingredient in temp_ingredients:
            print(f'{path}\\{temp_ingredient}')
            os.remove(f'{path}\\{temp_ingredient}')
        print('deleted')
        create_ingredients(path, name, time_for_cooking, count)
    else:
        print('not enough ingredients')
        time.sleep(time_for_cooking)  # временно


# join_ingredients(start_storage, ['muka', 'test', 'lemon'], 'box', 4, 5)
# create_ingredients(start_storage, 'bread', 3, 3)
