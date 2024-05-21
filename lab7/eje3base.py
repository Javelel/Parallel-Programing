# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:55:50 2024

@author: Irene
"""

import math

def compute_pi(n):
    h = 1.0 / n
    s = 0.0

    for i in range(n):
        x = h * (i + 0.5)
        s += 4.0 / (1.0 + x**2)
    return s * h

n = 100
pi = compute_pi(n)
error = abs(pi - math.pi)

print ("pi is approximately %.16f, error is %.16f" % (pi, error))