from random import randrange
from threading import Event, Thread
from time import ctime, sleep

runners = ['Pepe', 'Juan', 'Antonio', 'Andres', 'Pedro', 'Miguel']

start_event = Event()

def runner(name):
    sleep(randrange(1, 3))  # Random sleep to simulate preparation time
    print('%s Preparado para la carrera \n' % name)
    start_event.wait()  # Wait for the start event to be set
    print('%s Sale a: %s \n' % (name, ctime()))
    sleep(randrange(2, 5))  # Random sleep to simulate running time
    print('%s Llega a la meta a: %s \n' % (name, ctime()))

def salidacarrera():
    print('SALIDA!!!!!')
    start_event.set()  # Signal the start of the race

if __name__ == '__main__':
    threads = []
    print('Empezamos la carrera!!!!')
    for runner_name in runners:
        thread = Thread(target=runner, args=(runner_name,))
        threads.append(thread)
        thread.start()

    sleep(1)  # Simulate some delay before starting the race
    salidacarrera()

    for thread in threads:
        thread.join()
    print('FIN CARRERA!')
