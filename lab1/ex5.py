import threading

contador_naranjas = 0
repeticiones = 1000000
lock = threading.Lock()

def comprador():
    global contador_naranjas
    for i in range(repeticiones):
        with lock:
            contador_naranjas += 1

if __name__ == '__main__':
    jorge = threading.Thread(target=comprador)
    ana = threading.Thread(target=comprador)
    jorge.start()
    ana.start()
    jorge.join()
    ana.join()
    print("Tenemos: ", contador_naranjas, 'naranjas')
