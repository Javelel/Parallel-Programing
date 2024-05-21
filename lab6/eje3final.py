from mpi4py import MPI
import numpy as np
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10

assert n % size == 0, "n must be divisible by the number of processes."

data_local = np.empty(n // size, dtype=int)

if rank == 0:
    data_global = np.array([random.randint(1, 100) for _ in range(n)], dtype=int)
    print(f"Process {rank} distributes: {data_global}")
else:
    data_global = None

comm.Scatter([data_global, MPI.INT], data_local, root=0)

print(f"Process {rank} receives: {data_local}")