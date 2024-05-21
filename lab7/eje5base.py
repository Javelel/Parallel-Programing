# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:06:03 2024

@author: Irene
"""

import numpy as np
import matplotlib.pyplot as plt

def julia_set(z, c, max_iter):
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z**2 + c
    return max_iter

def generate_julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter):
    x_vals = np.linspace(xmin, xmax, width)
    y_vals = np.linspace(ymin, ymax, height)
    julia = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            x = x_vals[i]
            y = y_vals[j]
            z = complex(x, y)
            julia[j, i] = julia_set(z, c, max_iter)

    return julia

def plot_julia_set(julia_set,xmin, xmax, ymin, ymax):
    plt.imshow(julia_set, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.title("Conjunto de Julia")
    plt.xlabel("Parte real")
    plt.ylabel("Parte imaginaria")
    plt.show()
    
if __name__ == "__main__":
    xmin, xmax, ymin, ymax = -2, 2, -2, 2
    width, height = 500, 500
    c = complex(-0.7, 0.27015)
    max_iter = 300
    
    julia = generate_julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter)
    plot_julia_set(julia, xmin, xmax, ymin, ymax)

