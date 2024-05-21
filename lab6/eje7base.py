# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:50:16 2024

@author: Irene
"""

from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Cantidad de elementos que cada proceso generará
local_size = 5

# Generar datos aleatorios en cada proceso
local_data =[random.randint(1, 100) for _ in range(local_size)]
print(f"Proceso {rank} envia: {local_data}")


# Reunir los datos de todos los procesos en el proceso raíz
global_data=comm.gather(local_data, root=0)

# Imprimir los resultados en el proceso raíz
if rank == 0:
    print("Global data gathered from all processes:")
    print(global_data)