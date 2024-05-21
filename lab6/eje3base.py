# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:54:42 2024

@author: Irene
"""

from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Datos a distribuir
    n=10
    data = [random.randint(1, 100) for _ in range(n)]
    print(f"Proceso {rank} reparte: {data}")
else:
    data = None

# Distribuir los datos

data=comm.scatter(data, root=0)

# Cada proceso imprime su parte de los datos
print(f"Proceso {rank} recibe: {data}")