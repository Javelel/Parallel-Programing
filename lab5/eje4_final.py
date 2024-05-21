from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Total number of elements
n = 10000000

# Generate random numbers if rank is 0
if rank == 0:
    numbers = [random.randint(1, 100) for _ in range(n)]
    start_time = MPI.Wtime()

# Receive the list of numbers if rank is not 0
else:
    numbers = None

numbers = comm.bcast(numbers, root=0)

# Calculate sum of received numbers and display it
total_sum = sum(numbers)
print("Rank", rank, "sum:", total_sum)

# Measure communication time only for rank 0
if rank == 0:
    end_time = MPI.Wtime()  # End time measurement
    communication_time = end_time - start_time
    print("Communication time:", communication_time, "seconds")
