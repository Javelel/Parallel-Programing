from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0 or rank == size - 1:
	print("Hola mundo, soy el proceso ", rank, " de ", size)
