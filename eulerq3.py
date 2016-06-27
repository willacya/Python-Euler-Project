x = []

for i in range(1,13195/2):
	if 13195 % i == 0:
		x.append(i)

print max(x)

