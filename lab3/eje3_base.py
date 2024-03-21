import time 
import random 
from threading import Thread, Barrier, Semaphore

def moleculagenerada():
	print ("Generada una nueva molécula de H20") 
	time.sleep(0.5)

barrier = Barrier(3, action=moleculagenerada)
semaphore_H = Semaphore(2)
semaphore_O = Semaphore(1)


def Hidrogeno():
	#tiempo que tarda en generarse el atomo 
	time.sleep(random.randint(1, 4)) 
	print("H")
	semaphore_H.acquire()
	barrier.wait()
	semaphore_H.release()

def Oxigeno():
	#tiempo que tarda en generarse el atomo 
	time.sleep(random.randint(1, 4)) 
	print("O")
	semaphore_O.acquire()
	barrier.wait()
	semaphore_O.release()



if __name__ == '__main__': 
	listahilos = []   

	for i in range(10): 
		listahilos.append(Thread(target=Oxigeno)) 
	for j in range(10): 
		listahilos.append(Thread(target=Hidrogeno)) 
		
	for t in listahilos: 
		t.start()