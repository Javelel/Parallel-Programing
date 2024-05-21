import multiprocessing

def is_even(numbers, conn):
    for n in numbers:
        if n % 2 == 0:
            conn.send(n)
    conn.close()  # Close the connection after sending all data

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=is_even, args=(range(20), child_conn)) # Pass the child connection to the process

    p.start()
    p.join()

    while parent_conn.poll():  # Check if there's data in the pipe
        print(parent_conn.recv()) # Receive the data from the pipe

    parent_conn.close()  # Close the parent connection after receiving all data

