from collections import Counter

a = [12, 3, 4, 3, 5, 11, 12, 6, 7]

x = Counter(a)
print(x)

for i in x.keys():
	print(i, ":", x[i])
	
x_keys = list(x.keys())
x_values = list(x.values())

print(x_keys)
print(x_values)
