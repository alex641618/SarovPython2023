import matplotlib.pyplot as plt
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


def new_buff(bool_array, rule):

	s_rule = f'{rule:08b}'
	new_buff = bool_array.copy()

	for i in range(len(bool_array)):
		state = int(f'{int(bool_array[i - 1 + N if i - 1 < 0 else i - 1])}\
{int(bool_array[i])}{int(bool_array[i + 1 - N if i + 1 >= N  else i + 1])}', 2)

		match state:
			case 0:
				new_buff[i] = bool(int(s_rule[7]))
			case 1:
				new_buff[i] = bool(int(s_rule[6]))
			case 2:
				new_buff[i] = bool(int(s_rule[5]))
			case 3:
				new_buff[i] = bool(int(s_rule[4]))
			case 4:
				new_buff[i] = bool(int(s_rule[3]))
			case 5:
				new_buff[i] = bool(int(s_rule[2]))
			case 6:
				new_buff[i] = bool(int(s_rule[1]))
			case 7:
				new_buff[i] = bool(int(s_rule[0]))

	
	return new_buff


rule = np.ubyte(90)
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

for i in range(1, N):
	show_array[i] = new_buff(show_array[i-1], rule)

print('drawing...')
plt.imshow(show_array)
plt.show()
