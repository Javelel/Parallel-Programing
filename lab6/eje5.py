from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

random_number = np.random.randint(1, 101)

square = random_number ** 2

squares_received = comm.gather(square, root=0)

if rank == 0:
    total_sum = sum(squares_received)
    print("Total sum of squares:", total_sum)
