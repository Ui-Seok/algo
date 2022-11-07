n, m = map(int, input().split())
reserv_list = list()

for _ in range(m):
	a, b = input().split()
	
	if a == 'deposit':
		n += int(b)
		while reserv_list and n >= reserv_list[0]:
			n -= reserv_list[0]
			reserv_list.pop(0)
	elif a == 'pay':
		if n >= int(b):
			n -= int(b)
	else:
		if n >= int(b):
			n -= int(b)
		else:
			reserv_list.append(int(b))
				
print(n)