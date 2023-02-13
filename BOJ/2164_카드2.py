# 난이도: 실버 4
# 알고리즘 유형: 자료구조, 큐

"""
시작시간: 02:30
종료시간: 02:37
"""

from collections import deque

n = int(input())
arr = deque([i for i in range(1, n + 1)])

while len(arr) > 1:
    del arr[0]

    if len(arr) == 1:
        break
    else:
        pops = arr.popleft()
        arr.append(pops)

print(*arr)
