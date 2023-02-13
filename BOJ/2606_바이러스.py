# 난이도: 실버 3
# 알고리즘 유형: 그래프이론, 그래프탐색, 너비우선탐색, 깊이우선탐색

"""
시작시간: 03:58
종료시간: 04:06
"""

from collections import deque

n = int(input())
_map = int(input())
arr = dict()

for _ in range(_map):
    a, b = map(int, input().split())

    if arr.get(a) == None:
        arr[a] = [b]
    else:
        arr[a].append(b)

    if arr.get(b) == None:
        arr[b] = [a]
    else:
        arr[b].append(a)

visitied = [False for _ in range(n + 1)]
visitied[1] = True

q = deque()
q.append(1)
cnt = 0

while q:
    x = q.popleft()
    for i in arr[x]:
        if not visitied[i]:
            cnt += 1
            q.append(i)
            visitied[i] = True

print(cnt)
