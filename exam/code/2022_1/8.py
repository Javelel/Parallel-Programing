# Given the following code in MPI, explain what it does
# and modify it so that it uses collective communication
# instead of point-to-point communication.

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

N = 100

workloads = [0 for i in range(size)]
my_start = [0 for i in range(size)]
j=0

for i in range(size):
	workloads[i] = N // size
	my_start[i] = j
	j = j + workloads[i]

a = [1 for i in range(workloads[rank])]
b = [0 for i in range(workloads[rank])]

for i in range(workloads[rank]):
	b[i] = 1.0 + my_start[rank] + i

for i in range(workloads[rank]):
	a[i] = a[i] + b[i]

sum = 0
for i in range(workloads[rank]):
	sum+=a[i]

if rank == 0:
	world_sum = sum
	for i in range(1, size):
		sum_np = comm.recv(source=i)
		print('proceso: ', rank, 'recibe dato= ', sum_np, 'del procesador: ', i)
		world_sum += sum_np
		average = world_sum / N
	print('proceso: ', rank, 'media calculada= ', average)
else:
	print('proceso: ', rank, 'envia dato= ', sum)
	comm.send(sum, dest=0)