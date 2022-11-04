n, k = map(int, input().split())
bomb = 0

for _ in range(k):
	a, b = map(int, input().split())
	if n == 1:
		bomb += 1
	elif n == 2:
		bomb += 3
	else:
		if a == n and b == n:
			bomb += 3
		elif a == n or b == n:
			bomb += 4
		elif a == 1 and b == 1:
			bomb += 3
		elif a == 1 or b == 1:
			bomb += 4
		elif a == 1 and b == n:
			bomb += 3
		elif a == n and b == 1:
			bomb += 3
		else:
			bomb += 5
		
print(bomb)