# Regulate the following code with events
# so that the output is AABCCAABCCAABCCAABCC....... .
# The number of threads is not allowed to change,
# nor are functions A, B and C allowed to print more than one letter
# in each iteration (i.e. only one letter is printed
# in each iteration of the while loop).


import logging
import threading

LOG_FORMAT = "%(threadName)-17s %(levelname)-8s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def A():
	while True:
		logging.info("Ejecutando Hilo A")

def B():
	while True:
		logging.info("Ejecutando Hilo B")

def C():
	while True:
		logging.info("Ejecutando Hilo C")

if __name__ == "__main__":
	t1 = threading.Thread(target=A)
	t2 = threading.Thread(target=B)
	t3 = threading.Thread(target=C)

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()