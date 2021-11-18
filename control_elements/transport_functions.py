import os
from routes import *
import time


def move(start_location, end_location, time_for_move, count):
    items = os.listdir(start_location)
    # time.sleep(time_for_move)
    if len(items) == 0:
        print('empty')
    else:
        for item in items[:count:]:
            old_item = f'{start_location}\\{item}'
            print(old_item)
            os.rename(old_item, f'{end_location}\\{item}')
            time.sleep(time_for_move/count)


move(end_storage, start_storage, 5, 5)
