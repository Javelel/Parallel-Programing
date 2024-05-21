# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

def julia_set(z, c, max_iter):
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z**2 + c
    return max_iter

def generate_julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter, rank, size):
    x_vals = np.linspace(xmin, xmax, width)
    y_vals = np.linspace(ymin, ymax, height)
    julia_partial = np.zeros((height // size, width))

    start_row = rank * (height // size)
    end_row = (rank + 1) * (height // size)

    for i in range(width):
        for j in range(start_row, end_row):
            x = x_vals[i]
            y = y_vals[j]
            z = complex(x, y)
            julia_partial[j - start_row, i] = julia_set(z, c, max_iter)

    return julia_partial

def plot_julia_set(julia_set, xmin, xmax, ymin, ymax):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        julia_full = np.zeros((size * julia_set.shape[0], julia_set.shape[1]), dtype=np.float64)
    else:
        julia_full = None

    # Gather the partial results at the root process
    recvbuf = None
    if rank == 0:
        recvbuf = np.empty([size, julia_set.shape[0], julia_set.shape[1]], dtype=np.float64)

    # Gather the results from all processes
    comm.Gather(julia_set, recvbuf, root=0)

    if rank == 0:
        # Combine the results
        for i in range(size):
            julia_full[i * julia_set.shape[0]:(i + 1) * julia_set.shape[0], :] = recvbuf[i]

        # Plot the full Julia set
        plt.imshow(julia_full, cmap='hot', extent=(xmin, xmax, ymin, ymax))
        plt.colorbar()
        plt.title("Conjunto de Julia")
        plt.xlabel("Parte real")
        plt.ylabel("Parte imaginaria")
        plt.show()

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    xmin, xmax, ymin, ymax = -2, 2, -2, 2
    width, height = 500, 500
    c = complex(-0.7, 0.27015)
    max_iter = 300

    # Each process generates its part of the Julia set
    julia_partial = generate_julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter, rank, size)

    # Plot the full Julia set
    plot_julia_set(julia_partial, xmin, xmax, ymin, ymax)
