from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
	A=[1,2,3,4]
else:
	A=None

A = comm.scatter(A, root=0)
A += 1
B = comm.reduce(A, root=0)
A = comm.gather(A, root=0)

if rank == 0:
	print('Valor de A:', A)
	print('Valor de B:', B)