import time
import routes
import os
import re

storage = routes.end_storage
start_time = {
    'candies': time.time(),
    'chocolate': time.time(),
    'waffels': time.time()
}

average_times_for_candies = []
average_times_for_chocolate = []
average_times_for_waffels = []


def calc(name, times, product):
    items = os.listdir(storage)
    for item in items:
        if re.match(name, item):
            try:
                old_item = f'{storage}\\{item}'
                os.remove(old_item)
                temp_time = time.time() - start_time[product]
                times.append(temp_time)
                print(item, 'moved from storage')
                print('time for cooking:', '%.2f' % temp_time)
                print('average time:', '%.2f' % (sum(times) / len(times)), '\n')
                start_time[product] = time.time()
                break
            except:
                print(item, 'not found')


while True:
    calc('packed_candies', average_times_for_candies, 'candies')
    calc('packed_chocolate', average_times_for_chocolate, 'chocolate')
    calc('chocolate_waffles', average_times_for_waffels, 'waffels')
