from mpi4py import MPI
import random


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Total number of elements
n = 10

# Generate random numbers if rank is 0
if rank == 0:
    numbers = [random.randint(1, 100) for _ in range(n)]
    comm.send(numbers, dest=1)

# Receive the list of numbers and calculate sum if rank is 1
if rank == 1:
    numbers = comm.recv(source=0)
    total_sum = sum(numbers)
    comm.send(total_sum, dest=0)

# Receive the sum if rank is 0
if rank == 0:
    total_sum = comm.recv(source=1)
    print("Total sum:", total_sum)

# Wait for other processes
else:
    pass