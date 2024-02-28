import threading
import time
import random

libroA=threading.Lock()
libroB=threading.Lock()
libroC=threading.Lock()

def estudiante(nombre, primerlibro, segundolibro, repasos):
	while repasos>0:
		if not primerlibro.acquire(timeout=5):
			return
		
		print(" El estudiante: ", nombre, " tiene el primer libro")

		if not segundolibro.acquire(timeout=5):
			primerlibro.release()
			time.sleep(random.randint(1, 2))
			continue
		
		print(" El estudiante: ", nombre, " tiene el segundo libro")

		if repasos>0:
			repasos-=1
			time.sleep(random.randint(1, 3))
			print(" El estudiante: ", nombre, " ha repasado ")

		segundolibro.release()
		primerlibro.release()


if __name__ == '__main__':
	jorge=threading.Thread(target=estudiante, args=("Jorge", libroA, libroB,5))
	ana=threading.Thread(target=estudiante, args=("Ana", libroB, libroC,5))
	maria=threading.Thread(target=estudiante, args=("María", libroC, libroA,5))

	jorge.start()
	ana.start()
	maria.start()

	jorge.join()
	ana.join()
	maria.join()
	print("Hemos terminado de estudiar")