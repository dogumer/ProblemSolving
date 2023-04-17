myMap = {0: 0, 1:1 }

def fib(n):
	if n not in myMap:
		myMap[n] = fib(n-1) + fib(n-2)
	return myMap[n]

print(fib(2))
