from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

N = 100

workloads = [0 for _ in range(size)]
my_start = [0 for _ in range(size)]
j = 0

for i in range(size):
    workloads[i] = N // size
    my_start[i] = j
    j = j + workloads[i]

a = [1 for _ in range(workloads[rank])]
b = [0 for _ in range(workloads[rank])]

for i in range(workloads[rank]):
    b[i] = 1.0 + my_start[rank] + i

for i in range(workloads[rank]):
    a[i] = a[i] + b[i]

sum_local = sum(a)

# Perform reduction to get the global sum
global_sum = comm.allreduce(sum_local, op=MPI.SUM)

average = global_sum / N

print('proceso:', rank, 'media calculada:', average)
