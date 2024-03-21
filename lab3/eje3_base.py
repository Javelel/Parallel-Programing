import time 
import random 
from threading import Thread, Barrier, Lock

hydrogen_barrier = Barrier(2)
oxygen_barrier = Barrier(1)

def Hidrogeno():
	#tiempo que tarda en generarse el atomo 
	time.sleep(random.randint(1, 4)) 
	print("H")
	hydrogen_barrier.wait()

def Oxigeno():  
	#tiempo que tarda en generarse el atomo 
	time.sleep(random.randint(1, 4)) 
	print("O")
	oxygen_barrier.wait()

def moleculagenerada():
	with Lock():
		if(hydrogen_barrier.n_waiting == 0 and oxygen_barrier.n_waiting == 0):
			print ("Generada una nueva molécula de H20") 
			time.sleep(0.5)
			hydrogen_barrier.reset()
			oxygen_barrier.reset()

if __name__ == '__main__': 

	listahilos = []   

	for i in range(10): 
		listahilos.append(Thread(target=Oxigeno)) 
	for j in range(10): 
		listahilos.append(Thread(target=Hidrogeno)) 
		
	for t in listahilos: 
		t.start()
