import matplotlib.pyplot as plt
from mpi4py import MPI
import numpy as np
import sys

def fill_bool_array_by_number(bool_array, a):
	size = (sys.getsizeof(a) - 24)*8
	if (len(bool_array) == size):
		s_a = f'{a:0{size}b}'

		for i in range(size):
			bool_array[i] = bool(int(s_a[i]))

	else:
		print("Error: incorrect variable!")
		return bool_array

	return bool_array

def fill_bool_array_by_string(bool_array, string):
	len_a = len(bool_array)

	if (len_a == len(string)):

		for i in range(len_a):
			bool_array[i] = bool(int(string[i]))

	else:
		print("Error: incorrect len of string!")
		return bool_array

	return bool_array

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
	rule = np.ubyte(90)
	s_rule = f'{rule:08b}'
	
	string = \
	'00000000000000000000000000000000000000000000000000000000000000\
	000000000000000000000000000000000000000000000000000000000000000\
	000100000000000000000000000000000000000000000000000000000000000\
	000000000000000000000000000000000000000000000000000000000000000\
	000000'
	Ns = len(string)

	Na = 32 # Na = 2^n
	a = np.uint(65536) # need change if Na != 32

	print(f'Enter "1" if you want use {Na}-bit number or some other if you want use string')
	inp = input()

	if (inp == '1'):
		N = Na
	else:
		N = Ns

	bool_array = np.empty(N, dtype=np.bool_)

	if (inp == '1'):
		fill_bool_array_by_number(bool_array, a)
	else:
		fill_bool_array_by_string(bool_array, string)

	show_array = np.ndarray((N,N), dtype=np.bool_)
	show_array[0] = bool_array
else:
	s_rule = None
	show_array = None
	N = None

s_rule = comm.bcast(s_rule, root=0)
show_array = comm.bcast(show_array, root=0)
N = comm.bcast(N, root=0)
print(rank)
	
state = int(f'{int(show_array[0][rank - 1 + N if rank - 1 < 0 else rank - 1])}{int(show_array[0][rank])}{int(show_array[0][rank + 1 - N if rank + 1 >= N  else rank + 1])}', 2)

match state:
	case 0:
		show_array[1][rank] = bool(int(s_rule[7]))
	case 1:
		show_array[1][rank] = bool(int(s_rule[6]))
	case 2:
		show_array[1][rank] = bool(int(s_rule[5]))
	case 3:
		show_array[1][rank] = bool(int(s_rule[4]))
	case 4:
		show_array[1][rank] = bool(int(s_rule[3]))
	case 5:
		show_array[1][rank] = bool(int(s_rule[2]))
	case 6:
		show_array[1][rank] = bool(int(s_rule[1]))
	case 7:
		show_array[1][rank] = bool(int(s_rule[0]))
'''
if (rank == 14):
	print(f'rank={rank}')
	print(f'state={state}')
	print(f'show_array[{1}][{rank}]={show_array[1][rank]}')
'''

if rank == 0:
	print('drawing...')
	print(show_array[1])
	plt.imshow(show_array)
	#plt.show()
