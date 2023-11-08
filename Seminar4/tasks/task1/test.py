from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = 10
else:
    data = None

data = comm.bcast(data, root=0)

if rank == 0:
    #print('Process {} broadcast data:'.format(rank), data)
    data = data - 1
    print(data)
else:
    #print('Process {} received data:'.format(rank), data)
    data = data - 1
    print(data)