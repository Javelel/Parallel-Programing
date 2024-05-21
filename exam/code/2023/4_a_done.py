import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a = 1
b = 10000000

num_per_rank = b // size
summ = numpy.zeros(1)

temp = 0
lower_bound = a + rank * num_per_rank
upper_bound = a + (rank + 1) * num_per_rank
print("This is process ", rank, " and I am summing from ", lower_bound, " to ", upper_bound - 1, flush=True)

for i in range(lower_bound, upper_bound):
    temp += i

summ[0] = temp

total = numpy.zeros(1)

comm.Allreduce(summ, total, op=MPI.SUM)	# summ is the send buffer, total is the receive buffer

if rank == 0:
    # add the rest numbers to 10000000
    for i in range(a + (size) * num_per_rank, b + 1):
        total[0] = total[0] + i
    print("The sum of numbers from 1 to 10000000: ", int(total[0]))
