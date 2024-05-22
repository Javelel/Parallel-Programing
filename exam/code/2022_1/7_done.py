from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, lock):
	for _ in range(100):
		time.sleep(0.01)
		with lock: # Lock is used
			number.value += 1

def add_100_array(numbers, lock):
	for _ in range(100):
		time.sleep(0.01)
		with lock: # Lock is used
			for i in range(len(numbers)):
				numbers[i] += 1

if __name__ == '__main__':
	shared_number = Value('i', 0)
	print('Value at beginning is', shared_number.value)

	shared_array = Array('d', [0.0, 100.0, 200.0])
	print('Array at beginning:', shared_array[:])

	lock = Lock() # Lock is created

	process1 = Process(target=add_100, args=(shared_number, lock))
	process2 = Process(target=add_100, args=(shared_number, lock))
	process3 = Process(target=add_100_array, args=(shared_array, lock))

	process1.start()
	process2.start()
	process3.start()

	process1.join()
	process2.join()
	process3.join()

	print('Value at end is', shared_number.value)
	print('Array at end is', shared_array[:])
