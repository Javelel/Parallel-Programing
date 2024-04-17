import os
import urllib.request
import urllib.parse
import re
import shutil
import time
import multiprocessing

fich_total = 0
bytes_total = 0

def bajar_fichero(queue):
    global fich_total, bytes_total
    while True:
        direccion = queue.get()  # Get URL from the queue
        if direccion == "":
            break  # Terminate if an empty string is received
        id = multiprocessing.current_process().name
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

def bajar_html(url_raiz, queue):
    r = urllib.request.urlopen(url_raiz)
    html = r.read().decode('utf-8', 'ignore')
    for m in re.finditer(r'src\w*=\w*"([-_./0-9a-zA-Z]*)"', html, re.I):
        direccion = urllib.parse.urljoin(url_raiz, m.group(1))
        queue.put(direccion)  # Put URL into the queue

def main():
    url_raiz = 'http://www.uv.es'
    if not os.path.exists('download'):
        os.mkdir('download')

    queue = multiprocessing.Queue()

    # Create a fixed number of processes
    num_processes = os.cpu_count()
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=bajar_fichero, args=(queue,))
        p.start()
        processes.append(p)

    urls = []
    t1 = time.time()
    bajar_html(url_raiz, queue)

    # Add termination signals to the queue
    for _ in range(num_processes):
        queue.put("")

    # Wait for all processes to finish
    for p in processes:
        p.join()

    t2 = time.time()
    tiempo_total = t2 - t1

    print('---------------------')
    print('Tiempo', tiempo_total)
    print('Ficheros', fich_total)
    print('MBytes', bytes_total / (1024.0 ** 2))
    print('Ancho de banda (MBit/s)', (bytes_total * 8 / (1024.0 ** 2)) / tiempo_total)

if __name__ == "__main__":
    main()
