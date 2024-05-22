# a.	Explain what a barrier is and its methods.
# b.	Modify the code by replacing the barrier
# with another timing mechanism that simulates the exit of the runners.
# c.	Explain the synchronisation mechanism
# you have chosen in the previous section and the methods it has.


from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

runners = ['Pepe', 'Juan', 'Antonio', 'Andres', 'Pedro', 'Miguel']

def runner():
	name = runners.pop()
	sleep(randrange(1, 2))
	print('%s Preparado para la carrera \n' % name)
	salida.wait()
	print('%s Sale a: %s \n' % (name, ctime()))
	sleep(randrange(2, 5))
	print('%s Llega a la meta a: %s \n' % (name, ctime()))

def salidacarrera():
	print('SALIDA!!!!!')

if __name__ == '__main__':
	salida = Barrier(len(runners), salidacarrera)
	threads = []
	print('Empezamos la carrera!!!!')
	for i in range(len(runners)):
		threads.append(Thread(target=runner))
		threads[-1].start()

	for thread in threads:
		thread.join()
	print('FIN CARRERA!')