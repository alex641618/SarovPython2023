from include import items as item
import matplotlib.pyplot as plt

while True:
	try: 
		N = int(input("enter N: "))
	except ValueError:
		print('error: invalid N type')
		print('enter correct N again')
		continue
	break

print('item 1:')
random_ndarray = item.random_matrix_generator((N, N))
print(random_ndarray)

print('item 2:')
print(item.get_max(random_ndarray))

print('item 3:')
print('drawing a matrix...')
ax1 = item.create_matrix_im(random_ndarray, 1)
item.show_plot(ax1)

print('item 4:')
print('drawing an updated matrix...')
item.update_matrix_im(ax1)
item.show_plot(ax1)

print('item 5:')
print('drawing a matrix with cut circle...')
ndarray = item.cut_circle(random_ndarray)
ax2 = item.create_matrix_im(ndarray, 0)
item.show_plot(ax2)