def find_prime():
	prime_list = []
	i = 10001
	while len(prime_list) < 10002:
		isPrime = True
		for j in range(2, i):
			if i % j == 0:
				isPrime = False
		if isPrime:
			prime_list.append(i)
		i += 1
	print prime_list[-1]
	
find_prime()