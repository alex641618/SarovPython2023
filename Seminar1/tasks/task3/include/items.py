import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import pickle

save_dir = 'saves'

#item 1
def list_generator():
	return [i for i in range(0,99,2)]

#item 2
def list_reverser(arg_list):
	return arg_list[::-1]

#item 3
def list_saver_csv(arg_list, name):
	if not os.path.exists(save_dir):
		os.mkdir(save_dir)

	with open(os.path.join(save_dir, name), 'w', newline = '') as f:
		csv.writer(f, lineterminator = '').writerow(arg_list)
	print('list was saved as .csv file at directory \'saves\'')

#item 4
def list_saver_bin(arg_list, name):
	arg_bytes = bytes(arg_list)
	if not os.path.exists(save_dir):
		os.mkdir(save_dir)

	with open(os.path.join(save_dir, name), 'wb') as f:
		f.write(arg_bytes)
	print('list was saved as .bin file at directory \'saves\'')

#item 5
def list_saver_pickle(arg_list, name):
	if not os.path.exists(save_dir):
		os.mkdir(save_dir)

	with open(os.path.join(save_dir, name), 'wb') as f:
		pickle.dump(arg_list, f)
	print('list was saved as .pickle file at directory \'saves\'')

#item 6.1
def check_pickle(path):
	with open(path, 'rb') as f:
		return pickle.load(f)

#item 6.2
def check_bin(path):
	return np.fromfile(path, dtype = np.byte).tolist()

#item 6.3
def check_csv(path):
	with open(path, 'r') as f:
		return [eval(x) for sublist in list(csv.reader(f)) for x in sublist]

#item 7
def list_converter(arg_list):
	return np.array(arg_list)

#item 8
def square_ndarray(array):
	return array**2

#item 9, 10, 11, 12, 13
def draw_graph(y, x):
	plt.plot(x, y)
	plt.xlabel('x', fontsize = 16)
	plt.ylabel('y', fontsize = 16)
	plt.xticks(np.arange(0,100,10), fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.savefig(os.path.join(save_dir, 'plot.png'), dpi = 150)
	plt.savefig(os.path.join(save_dir, 'plot.pdf'), dpi = 150)
	plt.show()