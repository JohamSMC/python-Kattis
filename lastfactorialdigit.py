numberTimes=int(input())

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)


for element in range(numberTimes):
	num=int(input())
	aux=factorial(num)
	print(str(aux)[-1])


