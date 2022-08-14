'''
시작시간: 19시 47분
종료시간: 20시 45분
'''

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                start_x, start_y = i, j # start coordinate
            elif arr[i][j] == 3:
                end_x, end_y = i, j # end coordinate
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((start_x, start_y))
    visit = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]

    while q:
        x, y = q.popleft()
        visit[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                if (not visit[nx][ny]) and (arr[nx][ny] == 0):
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
                elif arr[nx][ny] == 3:
                    distance[end_x][end_y] = distance[x][y] 

    print('#{} {}'.format(tc, distance[end_x][end_y]))