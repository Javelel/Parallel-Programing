import os 
import urllib.request 
import urllib.parse 
import re 
import shutil 
import time 
import multiprocessing 

fich_total = 0 
bytes_total = 0 

def bajar_fichero(direccion): 
    global fich_total, bytes_total 
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

def bajar_html(url_raiz, urls): 
    r = urllib.request.urlopen(url_raiz) 
    html = r.read().decode('utf-8', 'ignore') 
    for m in re.finditer(r'src\w*=\w*"([-_./0-9a-zA-Z]*)"', html, re.I): 
        direccion = urllib.parse.urljoin(url_raiz, m.group(1)) 
        urls.append(direccion) 

def main(): 
    url_raiz = 'http://www.uv.es' 
    if not os.path.exists('download'): 
        os.mkdir('download') 

    urls = [] 
    t1 = time.time() 
    bajar_html(url_raiz, urls) 
    for direccion in urls: 
        bajar_fichero(direccion) 
    t2 = time.time() 
    tiempo_total = t2 - t1 

    print('---------------------') 
    print('Tiempo', tiempo_total) 
    print('Ficheros', fich_total) 
    print('MBytes', bytes_total / (1024.0 ** 2)) 
    print('Ancho de banda (MBit/s)', (bytes_total * 8 / (1024.0 ** 2)) / tiempo_total) 

if __name__ == "__main__": 
    main() 