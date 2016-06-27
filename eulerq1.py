x = [1,2]
y = 2
while x[-1] < 4000000:
	x.append(x[-1]+x[-2])
	if x[-1] % 2 == 0:
		y += x[-1]
		
print y
print x[-10:-1]

