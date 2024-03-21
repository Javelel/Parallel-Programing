import threading 
import time 
import random 

producto_disponible=False
reponer_event = threading.Event()

def cliente(id): 
    global producto_disponible 
    time.sleep(random.randint(0, 10))  # Simular llegada escalonada de clientes 
    print("Cliente ",id,"intentando comprar...") 
    if producto_disponible: 
        print("Cliente ",id, "producto comprado!") 
    else: 
        print("Cliente", id, "producto agotado. Esperando reposición.") 
        reponer_event.wait()  # Wait for replenishment
        if producto_disponible:  # Check availability after waiting
            print("Cliente", id, "producto comprado!") 
        else:
            print("Cliente", id, "producto agotado nuevamente. Saliendo.")  

def reponedor(): 
    global producto_disponible 

    for i in range(2): 
        print("Reponiendo producto...") 
        time.sleep(4)  # Simular tiempo de reposición 
        print("Producto disponible...") 
        producto_disponible = True
        reponer_event.set()  # Signal replenishment

        time.sleep(2)  # Simular fin existencias 
        print("Fin producto...") 
        producto_disponible = False
        reponer_event.clear()  # Reset event after depletion
 
def main(): 

    # Creamos hilos para simular varios clientes intentando comprar al mismo tiempo 
    hilos_clientes = [] 
    for i in range(5): 
        hilo_cliente = threading.Thread(target=cliente, args=(i,)) 
        hilos_clientes.append(hilo_cliente) 
        hilo_cliente.start() 

    # Simulamos el proceso de reposición del producto 
    hilo_reponedor = threading.Thread(target=reponedor) 
    hilo_reponedor.start() 

    # Esperamos a que todos los hilos terminen 
    for hilo_cliente in hilos_clientes: 
        hilo_cliente.join() 

    hilo_reponedor.join() 


if __name__ == "__main__": 
    main() 