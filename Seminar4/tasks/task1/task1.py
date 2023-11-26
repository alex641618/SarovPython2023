import matplotlib.pyplot as plt
from mpi4py import MPI
import numpy as np
import sys

def fill_bool_array_by_number(bool_array, a):
	size = (sys.getsizeof(a) - 24)*8
	if (len(bool_array) == size):
		s_a = f'{a:0{size}b}'

		for i in range(size):
			bool_array[i] = np.bool_(int(s_a[i]))

	else:
		print("Error: incorrect variable!")
		return bool_array

	return bool_array

def fill_bool_array_by_string(bool_array, string):
	len_a = len(bool_array)

	if (len_a == len(string)):

		for i in range(len_a):
			bool_array[i] = np.bool_(int(string[i]))

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

def new_buf(bool_array, rule, rank, size, j, N):
	s_rule = f'{rule:08b}'
	ghost_prev = np.bool_([0])
	ghost_past = np.bool_([0])

	if (size > N):

		if (rank != 1 and rank != N):
			comm.Recv([ghost_prev, 1, MPI.C_BOOL], source=rank-1, tag=rank-1)
			comm.Recv([ghost_past, 1, MPI.C_BOOL], source=rank+1, tag=rank+1)
		else:
			if (rank == 1):
				comm.Recv([ghost_prev, 1, MPI.C_BOOL], source=N, tag=N)
				comm.Recv([ghost_past, 1, MPI.C_BOOL], source=rank+1, tag=rank+1)	
			if (rank == N):
				comm.Recv([ghost_prev, 1, MPI.C_BOOL], source=rank-1, tag=rank-1)
				comm.Recv([ghost_past, 1, MPI.C_BOOL], source=1, tag=1)

	else:

		if (rank != 1 and rank != size - 1):
			comm.Recv([ghost_prev, 1, MPI.C_BOOL], source=rank-1, tag=rank-1)
			comm.Recv([ghost_past, 1, MPI.C_BOOL], source=rank+1, tag=rank+1)
		else:
			if (rank == 1):
				comm.Recv([ghost_prev, 1, MPI.C_BOOL], source=size-1, tag=size-1)
				comm.Recv([ghost_past, 1, MPI.C_BOOL], source=rank+1, tag=rank+1)	
			if (rank == size - 1):
				comm.Recv([ghost_prev, 1, MPI.C_BOOL], source=rank-1, tag=rank-1)
				comm.Recv([ghost_past, 1, MPI.C_BOOL], source=1, tag=1)

	new_buf = bool_array.copy()
	ex_buf = np.empty(len(new_buf)+2, dtype = np.bool_)

	ex_buf[1:len(new_buf)+1] = new_buf.copy()
	ex_buf[0] = ghost_prev
	ex_buf[len(ex_buf)-1] = ghost_past
	
	for i in range(1, len(ex_buf) - 1):
		state = int(f'{int(ex_buf[i - 1])}{int(ex_buf[i])}{int(ex_buf[i + 1])}', 2)

		match state:
			case 0:
				new_buf[i-1] = np.bool_((int(s_rule[7])))
			case 1:
				new_buf[i-1] = np.bool_((int(s_rule[6])))
			case 2:
				new_buf[i-1] = np.bool_((int(s_rule[5])))
			case 3:
				new_buf[i-1] = np.bool_((int(s_rule[4])))
			case 4:
				new_buf[i-1] = np.bool_((int(s_rule[3])))
			case 5:
				new_buf[i-1] = np.bool_((int(s_rule[2])))
			case 6:
				new_buf[i-1] = np.bool_((int(s_rule[1])))
			case 7:
				new_buf[i-1] = np.bool_((int(s_rule[0])))
	
	return new_buf

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

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

if rank == 0:
	print(f'Enter "1" if you want use {Na}-bit number or some other if you want use string')
	inp = input()	

	if (size == 1 or size == 2):
		if (inp == '1'):
			N = Na
		else:
			N = Ns

		show_array = np.ndarray((N,N), dtype=np.bool_)

		bool_array = np.empty(N, dtype=np.bool_)

		if (inp == '1'):
			fill_bool_array_by_number(bool_array, a)
		else:
			fill_bool_array_by_string(bool_array, string)

		show_array[0] = bool_array

		for i in range(1, N):
			show_array[i] = new_buff(show_array[i-1], rule)

		plt.imshow(show_array)
		plt.show()
		exit()

	else:
		for i in range(1, size):
			comm.send(inp, dest=i, tag=0)

else:
	if (rank == 1 and size == 2):
		exit()
	inp = comm.recv(source=0, tag=0)

if (inp == '1'):
	N = Na
else:
	N = Ns

bool_array = np.empty(N, dtype=np.bool_)

if (inp == '1'):
	fill_bool_array_by_number(bool_array, a)
else:
	fill_bool_array_by_string(bool_array, string)

if rank == 0:
	show_array = np.ndarray((N,N), dtype=np.bool_)
	show_array[0] = bool_array

for j in range(1, N):
	if (rank != 0):
		if (size > N):
			if rank < N + 1:
				n = 1
				n_last = 1
				buf = np.empty(n, dtype=np.bool_)
				buf[0] = bool_array[rank-1]
				
				if (rank == 1):
					ghost_prev = np.bool_(buf[0])
					comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=rank + 1, tag=rank) 
					ghost_past = np.bool_(buf[0])
					comm.Send([ghost_past, 1, MPI.C_BOOL], dest=N, tag=rank)
				elif (rank == N):
					ghost_prev = np.bool_(buf[0])
					comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=1, tag=rank) 
					ghost_past = np.bool_(buf[0])
					comm.Send([ghost_past, 1, MPI.C_BOOL], dest=rank - 1, tag=rank)
				else:
					ghost_prev = np.bool_(buf[0])
					comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=rank + 1, tag=rank) 
					ghost_past = np.bool_(buf[0])
					comm.Send([ghost_past, 1, MPI.C_BOOL], dest=rank - 1, tag=rank) 
			
				buf = new_buf(buf, rule, rank, size, j, N)
		
				comm.Send([buf, n, MPI.C_BOOL], dest=0, tag=rank)
			else:
				exit()
		elif (N%(size-1) == 0):
			n = int(N/(size-1))
			n_last = n
			buf = np.empty(n, dtype=np.bool_)
			buf = bool_array[(rank-1)*n:rank*n]

			if (rank == 1):
				ghost_prev = np.bool_(buf[n-1])
				comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=rank + 1, tag=rank) 
				ghost_past = np.bool_(buf[0])
				comm.Send([ghost_past, 1, MPI.C_BOOL], dest=size - 1, tag=rank)
			elif (rank == size - 1):
				ghost_prev = np.bool_(buf[n_last-1])
				comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=1, tag=rank) 
				ghost_past = np.bool_(buf[0])
				comm.Send([ghost_past, 1, MPI.C_BOOL], dest=rank - 1, tag=rank)
			else:
				ghost_prev = np.bool_(buf[n-1])
				comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=rank + 1, tag=rank) 
				ghost_past = np.bool_(buf[0])
				comm.Send([ghost_past, 1, MPI.C_BOOL], dest=rank - 1, tag=rank)

			buf = new_buf(buf, rule, rank, size, j, N)
	
			comm.Send([buf, n, MPI.C_BOOL], dest=0, tag=rank)
		else:
			n = int(N/(size))
			n_last = int(N%(size)) + 2*n

			if(rank!=size-1):
				buf = np.empty(n, dtype=np.bool_)
				buf = bool_array[(rank-1)*n:rank*n]
			else:
				buf = np.empty(n_last, dtype=np.bool_)
				buf = bool_array[len(bool_array) - n_last:len(bool_array)]
			if (rank == 1):
				ghost_prev = np.bool_(buf[n-1])
				comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=rank + 1, tag=rank) 
				ghost_past = np.bool_(buf[0])
				comm.Send([ghost_past, 1, MPI.C_BOOL], dest=size - 1, tag=rank)
			elif (rank == size - 1):
				ghost_prev = np.bool_(buf[n_last-1])
				comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=1, tag=rank) 
				ghost_past = np.bool_(buf[0])
				comm.Send([ghost_past, 1, MPI.C_BOOL], dest=rank - 1, tag=rank)
			else:
				ghost_prev = np.bool_(buf[n-1])
				comm.Send([ghost_prev, 1, MPI.C_BOOL], dest=rank + 1, tag=rank) 
				ghost_past = np.bool_(buf[0])
				comm.Send([ghost_past, 1, MPI.C_BOOL], dest=rank - 1, tag=rank)

			buf = new_buf(buf, rule, rank, size, j, N)
		
			if(rank!=size-1):	
				comm.Send([buf, n, MPI.C_BOOL], dest=0, tag=rank)
			else:
				comm.Send([buf, n_last, MPI.C_BOOL], dest=0, tag=rank)

		comm.Recv([bool_array, N, MPI.C_BOOL], source=0, tag=0)
	else:
		if (size > N):
			n = 1
			n_last = 1
			full_buf = np.empty(n*(N-1) + n_last, dtype=np.bool_)
			for i in range(1, N):
				comm.Recv([full_buf[n*(i-1):n*i], n, MPI.C_BOOL], source=i, tag=i)
			
			comm.Recv([full_buf[len(full_buf) - n_last:len(full_buf)], n_last, MPI.C_BOOL], source=N, tag=N)

			for i in range(1, N+1):
				comm.Send([full_buf, len(full_buf), MPI.C_BOOL], dest=i, tag=0)
		elif (N%(size-1) == 0):
			n = int(N/(size-1))
			n_last = n
			full_buf = np.empty(n*(size-2) + n_last, dtype=np.bool_)
			for i in range(1, size - 1):
				comm.Recv([full_buf[n*(i-1):n*i], n, MPI.C_BOOL], source=i, tag=i)

			comm.Recv([full_buf[len(full_buf) - n_last:len(full_buf)], n_last, MPI.C_BOOL], source=size - 1, tag=size - 1)
		
			for i in range(1, size):
				comm.Send([full_buf, len(full_buf), MPI.C_BOOL], dest=i, tag=0)
		else:
			n = int(N/(size))
			n_last = int(N%(size))
			n_last = n_last + 2*n

			full_buf = np.empty(n*(size-2) + n_last, dtype=np.bool_)
			for i in range(1, size - 1):
				comm.Recv([full_buf[n*(i-1):n*i], n, MPI.C_BOOL], source=i, tag=i)

			comm.Recv([full_buf[len(full_buf) - n_last:len(full_buf)], n_last, MPI.C_BOOL], source=size-1, tag=size-1)

			for i in range(1, size):
				comm.Send([full_buf, len(full_buf), MPI.C_BOOL], dest=i, tag=0)

		show_array[j] = full_buf.copy()

if (rank == 0):
	plt.imshow(show_array)
	plt.show()