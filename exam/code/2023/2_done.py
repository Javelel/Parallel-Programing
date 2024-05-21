import logging
import threading

LOG_FORMAT = "%(threadName)-17s %(levelname)-8s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Create events for synchronization
event_A1 = threading.Event()
event_A2 = threading.Event()
event_B = threading.Event()
event_C1 = threading.Event()  # Added event for second instance of C
event_C2 = threading.Event()

# Initialize events
event_A1.set()  # Start with A's first instance

def A():
    while True:
        event_A1.wait()  # Wait for the signal to print A
        logging.info("Ejecutando Hilo A")
        event_A1.clear()  # Clear the event for A's first instance
        event_A2.set()  # Signal A's second instance to run

        event_A2.wait()  # Wait for the signal to print A again
        logging.info("Ejecutando Hilo A")
        event_A2.clear()  # Clear the event for A's second instance
        event_B.set()  # Signal B to run

def B():
    while True:
        event_B.wait()  # Wait for the signal to print B
        logging.info("Ejecutando Hilo B")
        event_B.clear()  # Clear the event for B
        event_C1.set()  # Signal C's first instance to run

def C():
    while True:
        event_C1.wait()  # Wait for the signal to print C
        logging.info("Ejecutando Hilo C")
        event_C1.clear()  # Clear the event for C's first instance
        event_C2.set()  # Signal C's second instance to run

        event_C2.wait()  # Wait for the signal to print C again
        logging.info("Ejecutando Hilo C")
        event_C2.clear()  # Clear the event for C's second instance
        event_A1.set()  # Signal A's first instance to run again

if __name__ == "__main__":
    t1 = threading.Thread(target=A)
    t2 = threading.Thread(target=B)
    t3 = threading.Thread(target=C)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
