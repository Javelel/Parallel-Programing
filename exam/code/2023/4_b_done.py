# nie ogarniam o co w tym chodzi

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a = 1
b = 10000000

local_size = (b - a + 1) // size
local_start = rank * local_size + a
local_end = (rank + 1) * local_size + a
print("Process", rank, "will sum from", local_start, "to", local_end - 1)
if rank == size - 1:
    local_end = b + 1

local_sum = numpy.zeros(1)

local_temp = 0
for i in range(local_start, local_end):
    local_temp += i

local_sum[0] = local_temp

total_sum = numpy.zeros(1)
comm.Allreduce(local_sum, total_sum, op=MPI.SUM)

if rank == 0:
    for i in range(a + size * local_size, b + 1):
        total_sum[0] += i
    print("The sum of numbers from 1 to 10000000: ", int(total_sum[0]))
