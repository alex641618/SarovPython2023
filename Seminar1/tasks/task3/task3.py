from include import items as item
import numpy as np
import os

print('item 1:')
l = item.list_generator()
print(l)

print('item 2:')
lr = item.list_reverser(l)
print(lr)

print('item 3:')
item.list_saver_csv(lr, 'list.csv')

print('item 4:')
item.list_saver_bin(lr, 'list.bin')

print('item 5:')
item.list_saver_pickle(lr, 'list.pickle')

print('item 6:')
print('check pickle:')
print(item.check_pickle(os.path.join('saves', 'list.pickle')))
print('check bin-file:')
print(item.check_bin(os.path.join('saves', 'list.bin')))
print('check csv-file:')
print(item.check_csv(os.path.join('saves', 'list.csv')))

print('item 7:')
x = item.list_converter(lr)
print(x)

print('item 8:')
y = item.square_ndarray(x)
print(y)

print('item 9, 10, 11, 12, 13:')
item.draw_graph(y, x)
print('saving and drawing a graph...')