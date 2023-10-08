from include import items as item
import matplotlib.pyplot as plt
import numpy as np

print('item 1:')
t = item.create_t()
y = item.create_y(t)

print('drawing signal...')
fig = item.draw_yt(t, y)
fig = item.show_figure(fig)

print('item 2:')
w = item.create_w(t)
s = item.create_spectr(y)

print('drawing signal spectrum...')
item.draw_spectr(w, s, fig)
fig = item.show_figure(fig)