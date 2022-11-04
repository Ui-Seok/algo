t = int(input())

for _ in range(t):
	n = int(input())
	tests = list(map(int, input().split()))
	
	avg = sum(tests) / n
	cnt = 0
	
	for test in tests:
		if test >= avg:
			cnt += 1
	
	print(f'{cnt}/{n}')