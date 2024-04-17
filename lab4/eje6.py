import os 
import urllib.request 
import urllib.parse 
import re 
import shutil 
import time 
import multiprocessing 

def bajar_fichero(direccion): 
    id = multiprocessing.current_process().name 
    fichero = 'download/' + os.path.basename(urllib.parse.urlparse(direccion).path)
    try: 
        i = urllib.request.urlopen(direccion) 
        with open(fichero, 'wb') as f: 
            shutil.copyfileobj(i, f) 
            return f.tell()
    except Exception as err: 
        print(err)
        return 0

def bajar_html(url_raiz): 
    r = urllib.request.urlopen(url_raiz) 
    html = r.read().decode('utf-8', 'ignore') 
    urls = [] 
    for m in re.finditer(r'src\w*=\w*"([-_./0-9a-zA-Z]*)"', html, re.I): 
        direccion = urllib.parse.urljoin(url_raiz, m.group(1)) 
        urls.append(direccion) 
    return urls

def main(): 
    url_raiz = 'http://www.uv.es' 
    if not os.path.exists('download'): 
        os.mkdir('download') 

    t1 = time.time() 
    urls = bajar_html(url_raiz)
    
    # Use Pool.map() to run bajar_fichero in parallel
    with multiprocessing.Pool() as pool:
        results = pool.map(bajar_fichero, urls)
    
    t2 = time.time() 
    tiempo_total = t2 - t1 

    total_bytes = sum(results)
    fich_total = len(urls)

    print('---------------------') 
    print('Tiempo', tiempo_total) 
    print('Ficheros', fich_total) 
    print('MBytes', total_bytes / (1024.0 ** 2)) 
    print('Ancho de banda (MBit/s)', (total_bytes * 8 / (1024.0 ** 2)) / tiempo_total) 

if __name__ == "__main__": 
    main() 
