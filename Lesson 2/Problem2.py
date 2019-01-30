import time
numbers = [3, 5, 9, 17, 123, 666, 1000, 4321]

for number in numbers:
	number = number * 2
	print(str(number))
	time.sleep(0.2)

