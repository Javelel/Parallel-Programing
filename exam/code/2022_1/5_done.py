import threading

y = 0
r = 1
x = 2
z = 0

# Create an event for synchronization
h2_done = threading.Event()

def H1():
    global x, y, r
    # Wait until H2 signals it is done
    h2_done.wait()
    y = x
    r += 2

def H2():
    global x, r
    r += 1
    x += 1
    # Signal that H2 is done
    h2_done.set()

def H3():
    global z
    z += 5

def main():
    t1 = threading.Thread(target=H1)
    t2 = threading.Thread(target=H2)
    t3 = threading.Thread(target=H3)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("Valor y: ", y)
    print("Valor r: ", r)
    print("Valor x: ", x)
    print("Valor z: ", z)

if __name__ == '__main__':
    main()
