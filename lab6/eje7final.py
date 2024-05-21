from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Cantidad de elementos que cada proceso generará
local_size = 5

# Generar datos aleatorios en cada proceso
local_data = np.random.randint(1, 101, local_size)
print(f"Proceso {rank} envia: {local_data}")

if rank == 0:
    global_data = np.empty((size, local_size), dtype=int)
else:
    global_data = None

# Reunir los datos de todos los procesos en el proceso raíz
comm.Gather(local_data, global_data, root=0)

# Imprimir los resultados en el proceso raíz
if rank == 0:
    print("Global data gathered from all processes:")
    print(global_data)
