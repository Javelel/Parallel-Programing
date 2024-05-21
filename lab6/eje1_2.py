from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10

if rank == 0:
    numbers = np.random.randint(1, 101, n)
    comm.Send(numbers, dest=1)

if rank == 1:
    numbers = np.empty(n, dtype=int)
    comm.Recv(numbers, source=0)
    total_sum = np.sum(numbers)
    total_sum_vector = np.array([total_sum], dtype=int)
    comm.Send(total_sum_vector, dest=0)

if rank == 0:
    total_sum_vector = np.empty(1, dtype=int)
    comm.Recv(total_sum_vector, source=1)
    print("Total sum:", total_sum_vector[0])

else:
    pass
