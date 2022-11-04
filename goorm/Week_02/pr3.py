N, K = list(map(int, input().split()))
arr = list()

for _ in range(N):
	name, height = list(input().split())
	arr.append([name, float(height)])

arr.sort(key=lambda x : (x[0], x[1]))

print('{} {:.2f}'.format(arr[K-1][0], arr[K-1][1]))
