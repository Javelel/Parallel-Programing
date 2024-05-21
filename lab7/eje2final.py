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

##########################################################################

# Define the number of elements each process will receive and their offsets
counts = [3, 2, 1, 4]
displacements = [3, 7, 10, 12]

# Initialize the local array for each process
if rank == 0:
    array_local = numpy.empty(3, dtype='i')
elif rank == 1:
    array_local = numpy.empty(2, dtype='i')
elif rank == 2:
    array_local = numpy.empty(1, dtype='i')
elif rank == 3:
    array_local = numpy.empty(4, dtype='i')
# Scattering of B from P2
comm.Scatterv([B, counts, displacements, MPI.INT], array_local, root=2)

# Local calculation
array_local += 100
    
# Gathering of Bloc in P2
comm.Gatherv(array_local, [B, counts, displacements, MPI.INT], root=2)

# Print results
if rank == 2:
    print("\n B in rank=2 after the calculation \n")
    for i in range(16):
        print("%4d" % B[i], end="")
    print("\n\n")
