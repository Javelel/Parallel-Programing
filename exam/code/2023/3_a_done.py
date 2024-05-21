import multiprocessing

def is_even(numbers, q):
    for n in numbers:
        if n % 2 == 0:
            q.put(n)

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=is_even, args=(range(20), q))

    p.start()
    p.join()

    # Loop until the queue is empty
    while not q.empty():
        print(q.get())
