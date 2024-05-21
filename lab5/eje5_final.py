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
    start_time_broadcast = MPI.Wtime()
else:
    numbers = None

# Broadcast the list of numbers from rank 0 to all other processes
numbers = comm.bcast(numbers, root=0)

# Calculate sum of received numbers
partial_sum = sum(numbers)

# Gather partial sums from all processes to process 0
if rank == 0:
    start_time_reduction = MPI.Wtime()
    partial_sums = [partial_sum]
    for i in range(1, size):
        partial_sum_received = comm.recv(source=i)
        partial_sums.append(partial_sum_received)
    total_sum_point_to_point = sum(partial_sums)
    end_time_point_to_point = MPI.Wtime()
else:
    comm.send(partial_sum, dest=0)

# Use MPI reduction function to calculate total sum
total_sum_reduction = comm.reduce(partial_sum, op=MPI.SUM, root=0)

# Show sums calculated with both communication methods and their execution times
if rank == 0:
    end_time_reduction = MPI.Wtime()  # End time measurement for reduction
    communication_time_point_to_point = end_time_point_to_point - start_time_broadcast
    reduction_time = end_time_reduction - start_time_reduction
    print("Total sum using point-to-point communication:", total_sum_point_to_point)
    print("Total sum using MPI reduction function:", total_sum_reduction)
    print("Communication time using point-to-point communication:", communication_time_point_to_point, "seconds")
    print("Reduction time using MPI reduction function:", reduction_time, "seconds")
