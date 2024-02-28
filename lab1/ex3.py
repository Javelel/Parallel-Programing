import random
import time
import numpy

def multiplicar(n, a, b, c):
	for i in range(n):
		for j in range(n):
			d = 0
			for k in range(n):
				d = d + a[j,k] * b[k,i]
			c[i,j] = d

k = [100, 200, 300, 400, 500]
random.seed(0)

for n in k:
	a = numpy.array([[random.random() for i in range(n)]
	for j in range(n)])
	b = numpy.array([[random.random() for i in range(n)]
	for j in range(n)])
	c = numpy.zeros((n,n))
	tiempo = []
	
	for r in range(3):
		t1 = time.perf_counter()
		multiplicar(n, a, b, c)
		t2 = time.perf_counter()
		print("Tiempo [", r, "]", t2 - t1)
		tiempo.append(t2 - t1)
	print("Tamaño", n, "Tiempo mínimo", min(tiempo))