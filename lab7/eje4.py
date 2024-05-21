# -*- coding: utf-8 -*-

from mpi4py import MPI
import numpy as np
import math

def compute_pi_partial(start, end, step, h):
    s = np.float64(0.0)
    for i in range(start, end, step):
        x = h * (i + 0.5)
        s += 4.0 / (1.0 + x**2)
    return s

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Total number of intervals
n = 100
h = np.float64(1.0 / n)

# Each process computes its part of the sum using cyclic distribution
partial_sum = compute_pi_partial(rank, n, size, h)

# Convert partial_sum to numpy scalar
partial_sum = np.array(partial_sum)

# Reduce the partial sums to get the final sum in the root process
total_sum = np.array(0.0)
comm.Reduce([partial_sum, MPI.DOUBLE], [total_sum, MPI.DOUBLE], op=MPI.SUM, root=0)

if rank == 0:
    pi = total_sum * h
    error = abs(pi - math.pi)
    print("pi is approximately %.16f, error is %.16f" % (pi, error))
