import math
c = []

y = 600851475143
x = int(math.sqrt(y))
for i in range (2, x):
	if y % i == 0:
		isPrime = True
		for j in range(2,i):
			if i % j == 0:
				isPrime = False
		if isPrime:
			c.append(i)

print c