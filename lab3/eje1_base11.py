import os
import urllib.request
import urllib.parse
import re
import shutil
import time
import threading

fich_total = 0
bytes_total = 0

def bajar_fichero(direccion):
    global fich_total, bytes_total
    id = threading.current_thread().name
    fich_total += 1
    print(id, fich_total, direccion)
    s = direccion.split('/')
    fichero = 'download/' + s[-1]
    try:
        i = urllib.request.urlopen(direccion)
        with open(fichero, 'wb') as f:
            shutil.copyfileobj(i, f)
            bytes_total += f.tell()
    except Exception as err:
        print(err)

def consumidor(urls, semaforo, semaforo2):
    while True:
        semaforo.acquire()
        if len(urls) == 0: return
        bajar_fichero(urls.pop())
        semaforo2.release()

def bajar_html(url_raiz, urls, semaforo, semaforo2):
    r = urllib.request.urlopen(url_raiz)
    html = r.read().decode('utf-8', 'ignore')
    for m in re.finditer(r'src\w*=\w*"([-_./0-9a-zA-Z]*)"', html, re.I):
        semaforo2.acquire()
        direccion = urllib.parse.urljoin(url_raiz, m.group(1))
        urls.append(direccion)
        semaforo.release()

def main():
    url_raiz = 'http://www.uv.es'
    if not os.path.exists('download'):
        os.mkdir('download')

    urls = []
    hilos = []
    semaforo = threading.Semaphore(0)
    semaforo2 = threading.Semaphore(10)

    t1 = time.time()

    # crear hilo productor
    p = threading.Thread(target=bajar_html, args=(url_raiz, urls, semaforo, semaforo2))
    p.start()

    # crear hilos consumidores
    for i in range(4):
        h = threading.Thread(target=consumidor, args=(urls, semaforo, semaforo2))
        hilos.append(h)
        h.start()

    # esperar a que los hilos terminen
    p.join()
    for h in hilos:
        semaforo.release()
    for h in hilos:
        h.join()

    t2 = time.time()
    tiempo_total = t2 - t1

    print('---------------------')
    print('Tiempo', tiempo_total)
    print('Ficheros', fich_total)
    print('MBytes', bytes_total / (1024.0 ** 2))
    print('Ancho de banda (MBit/s)', (bytes_total * 8 / (1024.0 ** 2))
                                     / tiempo_total)

if __name__ == "__main__":
    main()