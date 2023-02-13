# 난이도: 실버 5
# 알고리즘 유형: 자료구조, 우선순위 큐

"""
시작시간: 01:28
종료시간: 01:35
"""


import heapq
import sys

input = sys.stdin.readline
n = int(input())

arr = list()
for _ in range(n):
    a = int(input())
    if a == 0:
        if not arr:
            print(0)
        else:
            item = heapq.heappop(arr)
            print(item)
    else:
        heapq.heappush(arr, a)
