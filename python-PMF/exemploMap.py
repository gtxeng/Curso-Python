kph = [40, 50, 56, 64, 73, 79, 85, 96, 100, 120]
mph = []
for i in kph:
	mph.append(i/1.61)
print(mph)
mph2 = list(map(lambda x: x/1.61,kph))
print(mph2)