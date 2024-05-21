from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Datos a distribuir
    n = 101
    tamanyos = np.full(size, n // size, dtype=int)
    tamanyos[:n % size] += 1
    data_global = np.random.randint(1, 101, n)
    print(f"Proceso {rank} reparte: {data_global}")
else:
    tamanyos = np.empty(size, dtype=int)
    data_global = None

comm.Bcast(tamanyos, root=0)

size_local = tamanyos[rank]
data_local = np.empty(size_local, dtype=int)

comm.Scatterv([data_global, tamanyos], data_local, root=0)

print(f"Proceso {rank} recibe: {data_local}")
