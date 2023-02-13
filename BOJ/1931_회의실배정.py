# 난이도: 실버 1
# 알고리즘 유형: 그리디, 정렬

"""
시작시간: 00:54
종료시간: 01:18
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr = sorted(arr, key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0

for start, end in arr:
    if end_time <= start:
        cnt += 1
        end_time = end

print(cnt)
