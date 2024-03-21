import time 
import random 
from threading import Thread 

def Hidrogeno(): 
    #tiempo que tarda en generarse el atomo 
    time.sleep(random.randint(1, 4)) 
    print("H") 

def Oxigeno():  
    #tiempo que tarda en generarse el atomo 
    time.sleep(random.randint(1, 4)) 
    print("O") 

def moleculagenerada(): 
    print ("Generada una nueva molécula de H20") 
    time.sleep(0.5) 
   

if __name__ == '__main__': 

    listahilos = []   

    for i in range(10): 
        listahilos.append(Thread(target=Oxigeno)) 
    for j in range(10): 
        listahilos.append(Thread(target=Hidrogeno)) 
        
    for t in listahilos: 
        t.start()