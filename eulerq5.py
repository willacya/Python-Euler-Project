def find_factor(num):
	factor = True
	for i in range(1,21):
		if num % i != 0:
			factor = False
	return factor
	
count = 1
while find_factor(count) == False:
	count += 1
	
print count