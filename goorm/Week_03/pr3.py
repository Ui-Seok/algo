from collections import deque

n, m, k = map(int, input().split())

graph = dict()

for n = int(input())
s = list(input())

phone = {'1': ['1', '.', ',', '?', '!'],
		 '2': ['2', 'A', 'B', 'C'],
		 '3': ['3', 'D', 'E', 'F'],
		 '4': ['4', 'G', 'H', 'I'],
		 '5': ['5', 'J', 'K', 'L'],
		 '6': ['6', 'M', 'N', 'O'],
		 '7': ['7', 'P', 'Q', 'R', 'S'],
		 '8': ['8', 'T', 'U', 'V'],
		 '9': ['9', 'W', 'X', 'Y', 'Z']}

start = s[0]
cnt = 0
answer = ''

for i in range(n):
	if start == s[i]:
		cnt += 1
	else:
		if start == '1' or start == '7' or start == '9':
			cnt = cnt % 5
			if cnt == 0:
				cnt = 5
		else:
			cnt = cnt % 4
			if cnt == 0:
				cnt = 4
				
		answer += phone[start][cnt-1]
		start = s[i]
		cnt = 1

if start == '1' or start == '7' or start == '9':
	cnt = cnt % 5
	if cnt == 0:
		cnt = 5
else:
	cnt = cnt % 4
	if cnt == 0:
		cnt = 4
				
answer += phone[start][cnt-1]

print(answer)_ in range(m):
	a, b = map(int, input().split())
	
	if graph.get(a) == None:
		graph[a] = [b]
	else:
		graph[a].append(b)
		
	if graph.get(b) == None:
		graph[b] = [a]
	else:
		graph[b].append(a)

q = deque()
q.append(1)

visited = [0 for _ in range(n+1)]
visited[1] = 1

cnt = 0

while q:
	start = q.popleft()
	
	if start == n:
		break
		
	for i in graph[start]:
		if visited[i] == 0:
			q.append(i)
			visited[i] = visited[start] + 1
			
answer = visited[n] - 1

if answer > k:
	print('NO')
elif answer < 0:
	print('NO')
else:
	print('YES')