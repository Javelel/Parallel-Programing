import random
import time

def multiplicar(n, a, b, c):
	for i in range(n):
		for j in range(n):
			d = 0
			for k in range(n):
				d = d + a[j][k] * b[k][i]
			c[i][j] = d

# n = 500
n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
random.seed(0)
for k in n:
	a = [[random.random() for i in range(k)] for j in range(k)]
	b = [[random.random() for i in range(k)] for j in range(k)]
	c = [[0 for i in range(k)] for j in range(k)]

	tiempo = []
	for r in range(3):
		t1 = time.perf_counter()
		multiplicar(k, a, b, c)
		t2 = time.perf_counter()
		print("Tiempo [", r, "]", t2 - t1)
		tiempo.append(t2 - t1)

	print("Tamaño", k, "Tiempo mínimo", min(tiempo))