# a.	Indicate the output produced by the code.
# Why does it not match the desired output?
# b.	Explain what the objects Value and Array are
# and what they are used for. Justify their use in the code.
# c.	Modify the code so that the output is as expected.

from multiprocessing import Process, Value, Array
import time

def add_100(number):
	for _ in range(100):
		time.sleep(0.01)
		number += 1

def add_100_array(numbers):
	for _ in range(100):
		time.sleep(0.01)
		for i in range(len(numbers)):
			numbers[i] += 1

if __name__ == '__main__':
	shared_number = Value('i', 0)
	print('Value at beginning is', shared_number)

	shared_array = Array('d', [0.0, 100.0, 200.0])
	print('Array at beginning:', shared_array[:])

	process1 = Process(target=add_100, args=(shared_number,))
	process2 = Process(target=add_100, args=(shared_number,))
	process3 = Process(target=add_100_array, args=(shared_array,))

	process1.start()
	process2.start()
	process3.start()

	process1.join()
	process2.join()
	process3.join()

	print('Value at end:', shared_number)
	print('Array at end:', shared_array[:])

	# Value at beginning: 0
	# Array at beginning: [0.0, 100.0, 200.0]
	# Value at end: 200
	# Array at end: [100.0, 200.0, 300.0]
