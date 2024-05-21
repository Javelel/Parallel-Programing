from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Determine the number of elements each process should receive
n = 101
tamanyos = np.full(size, n // size, dtype=int)
tamanyos[:n % size] += 1

# Use MPI_Allgather to share the size information with all processes
all_tamanyos = np.empty(size, dtype=int)
comm.Allgather([tamanyos[rank], MPI.INT], [all_tamanyos, MPI.INT])

# Each process now knows how much data it should receive
size_local = all_tamanyos[rank]
data_local = np.empty(size_local, dtype=int)

# Process 0 prepares the data to distribute
if rank == 0:
    data_global = np.random.randint(1, 101, n)
    print(f"Proceso {rank} reparte: {data_global}")
else:
    data_global = None

# Distribute the data using Scatterv
comm.Scatterv([data_global, all_tamanyos, MPI.INT], data_local, root=0)

print(f"Proceso {rank} recibe: {data_local}")
