import random
import time
import multiprocessing

# Dodajemy argument 'n' do funkcji, żeby uniknąć błędu z niezdefiniowaną zmienną
def multiplicar(i, j):
	d = 0
	for k in range(n):
		d += a[j][k] * b[k][i]
	return d

def lista_a_matriz(l, n):
	return [l[i:i+n] for i in range(0, len(l), n)]

n = 500
np = [1, 2, 4, 6, 8]

random.seed(0)

a = [[random.random() for i in range(n)] for j in range(n)]
b = [[random.random() for i in range(n)] for j in range(n)]
c = [[0 for i in range(n)] for j in range(n)]

if __name__ == '__main__':
	
	
	for k in np:
		tiempo = []
		with multiprocessing.Pool(k) as p:
			for r in range(3):
				t1 = time.perf_counter()
				l = []
				for i in range(n):
					for j in range(n):
						# Do każdej iteracji dodajemy 'n' oraz macierze 'a' i 'b' jako argumenty
						l.append((i, j))
				# Funkcja 'multiplicar' otrzymuje teraz 'n', 'a', 'b' jako argumenty
				s = p.starmap(multiplicar, l)
				c = lista_a_matriz(s, n)
				t2 = time.perf_counter()
				print(f"Tiempo [{r}]: {t2 - t1}")
				tiempo.append(t2 - t1)
		print(f"Procesos: {k}, Tamaño: {n}, Tiempo mínimo: {min(tiempo)}")
	