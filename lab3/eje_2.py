import os
import urllib.request
import urllib.parse
import re
import shutil
import time
import threading
import queue

fich_total = 0
bytes_total = 0
lock = threading.Lock()

def bajar_fichero(urls):
	global fich_total, bytes_total
	id = threading.current_thread().name
	while True:
		try:
			direccion = urls.get(timeout=1)
		except queue.Empty:
			return
		with lock:
			fich_total += 1
		print(id, fich_total, direccion)
		s = direccion.split('/')
		fichero = 'download/' + s[-1]
		try:
			i = urllib.request.urlopen(direccion)
			with open(fichero, 'wb') as f:
				shutil.copyfileobj(i, f)
				with lock:
					bytes_total += f.tell()
		except Exception as err:
			print(err)

def bajar_html(url_raiz, urls):
	r = urllib.request.urlopen(url_raiz)
	html = r.read().decode('utf-8', 'ignore')
	for m in re.finditer(r'src\w*=\w*"([-_./0-9a-zA-Z]*)"', html, re.I):
		direccion = urllib.parse.urljoin(url_raiz, m.group(1))
		urls.put(direccion)

def main():
	url_raiz = 'http://www.uv.es'
	if not os.path.exists('download'):
		os.mkdir('download')

	urls = queue.Queue()
	hilos = []

	t1 = time.time()

	# crear hilo productor
	p = threading.Thread(target=bajar_html, args=(url_raiz, urls), daemon=True)
	p.start()

	# crear hilos consumidores
	for i in range(4):
		h = threading.Thread(target=bajar_fichero, args=(urls,), daemon=True)
		hilos.append(h)
		h.start()

	# esperar a que los hilos terminen
	p.join()
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