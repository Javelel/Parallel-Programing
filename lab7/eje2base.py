# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:23:00 2024

@author: Irene
"""

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 2:
    B=numpy.empty(16, dtype='i')
    for i in range(16):
        B[i] = i
else:
    B=None

# Scattering of B from P2


# Local calculation

    
# Gathering of Bloc in P2


# Print results
if rank == 2:
    print("\n B in rank=2 after the calculation \n")
    for i in range(16):
        print("%4d" % B[i], end="")
    print("\n\n")
