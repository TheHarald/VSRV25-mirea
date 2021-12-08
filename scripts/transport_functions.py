import os
import time
import re


def move(start_location, end_location, time_for_move, count):
    items = os.listdir(start_location)
    time.sleep(time_for_move)
    if len(items) == 0:
        print('empty')
    else:
        for item in items[:count:]:
            old_item = f'{start_location}\\{item}'
            print(old_item)
            os.rename(old_item, f'{end_location}\\{item}')
            # time.sleep(time_for_move/count)


def find_and_move(start_location, end_location, name, time_for_move):
    items = os.listdir(start_location)
    time.sleep(time_for_move)
    if len(items) == 0:
        print('empty')
        print(name, 'not found')
    for item in items:
        if re.match(name, item):
            try:
                old_item = f'{start_location}\\{item}'
                os.rename(old_item, f'{end_location}\\{item}')
                print(item, 'moved')
                break
            except:
                print(item, 'not found')


