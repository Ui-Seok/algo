# 난이도: 실버 5
# 알고리즘 유형: 정렬

"""
시작시간: 03:18
종료시간: 03:26
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = sorted(arr, key=lambda x: (x[0], x[1]))

for ar in arr:
    print(*ar)
