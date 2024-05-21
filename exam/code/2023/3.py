# a.	If we run the code we see that it never finishes.
# Explain why this happens and how you would fix it.

# b.	Modify the code to use a pipeline
# instead of a queue for process communication,
# ensuring that the code terminates correctly.

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

	while q:
		print(q.get())

# a) The while loop is always true, even when the queue is empty.