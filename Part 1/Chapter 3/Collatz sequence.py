def collatz(number):
	global a
	if number % 2 == 1:
		a = 3 * number + 1
		print(a)
	elif number % 2 == 0:
		a = number // 2
		print(a)

a = 0
print('Enter number: ')
while True:
	if a == 1:
		break
	else:
		number = int(input())			
		collatz(number)

