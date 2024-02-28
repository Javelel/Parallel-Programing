import os
import urllib.request
import urllib.parse
import re
import shutil
import time
import threading
from queue import Queue

fich_total = 0
bytes_total = 0
NUM_CONSUMERS = 4
urls_queue = Queue()

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

def bajar_html(url_raiz, urls, semaphore):
	r = urllib.request.urlopen(url_raiz)
	html = r.read().decode('utf-8', 'ignore')
	for m in re.finditer(r'src\w*=\w*"([-_./0-9a-zA-Z]*)"', html, re.I):
		direccion = urllib.parse.urljoin(url_raiz, m.group(1))
		urls.put(direccion)
		semaphore.release()

def producer(url_root, urls, semaphore):
	bajar_html(url_root, urls, semaphore)
	for _ in range(NUM_CONSUMERS):
		semaphore.release()

def consumer(urls, semaphore):
	while True:
		semaphore.acquire()
		address = urls.get()
		if address is None:
			break
		bajar_fichero(address)
		urls.task_done()

def main():
	url_raiz = 'http://www.uv.es'
	if not os.path.exists('download'):
		os.mkdir('download')

	urls = Queue()
	semaphore = threading.Semaphore(0)

	t1 = time.time()

	consumer_threads = []
	for _ in range(NUM_CONSUMERS):
		thread = threading.Thread(target=consumer, args=(urls, semaphore))
		consumer_threads.append(thread)
		thread.start()

	producer_thread = threading.Thread(target=producer, args=(url_raiz, urls, semaphore))
	producer_thread.start()

	producer_thread.join()

	for _ in range(NUM_CONSUMERS):
		urls.put(None)

	for thread in consumer_threads:
		thread.join()

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
