from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10000000

if rank == 0:
    numbers = np.random.randint(1, 101, n)
    start_time = MPI.Wtime()
    comm.Bcast(numbers, root=0)
    end_time = MPI.Wtime()
    communication_time = end_time - start_time
    print("Communication time:", communication_time, "seconds")
else:
    numbers = np.empty(n, dtype=int)
    comm.Bcast(numbers, root=0)

comm.barrier()
# bcast