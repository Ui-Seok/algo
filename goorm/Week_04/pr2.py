import copy

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
copy_maps = copy.deepcopy(maps)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

day = 0

while sum(sum(maps[i]) for i in range(n)) != 0:
	day += 1
	for x in range(n):
		for y in range(n):
			if maps[x][y] != 0:
				cnt = 0
				for i in range(4):
					nx = x + dx[i]
					ny = y + dy[i]
					if 0 <= nx < n and 0 <= ny < n:
						if maps[nx][ny] == 0:
							cnt += 1
				if maps[x][y] >= cnt:
					copy_maps[x][y] -= cnt
				else:
					copy_maps[x][y] = 0
	maps = copy.deepcopy(copy_maps)
print(day)