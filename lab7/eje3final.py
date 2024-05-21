# -*- coding: utf-8 -*-

from mpi4py import MPI
import math

def compute_pi_partial(start, end, step, h):
    s = 0.0
    for i in range(start, end, step):
        x = h * (i + 0.5)
        s += 4.0 / (1.0 + x**2)
    return s

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Total number of intervals
n = 100
h = 1.0 / n

# Each process computes its part of the sum using cyclic distribution
partial_sum = compute_pi_partial(rank, n, size, h)

# Reduce the partial sums to get the final sum in the root process
total_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)

if rank == 0:
    pi = total_sum * h
    error = abs(pi - math.pi)
    print("pi is approximately %.16f, error is %.16f" % (pi, error))
