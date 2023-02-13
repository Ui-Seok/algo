# 난이도: 실버 5
# 알고리즘 유형: 정렬

"""
시작시간: 04:23
종료시간: 04:31
"""

n = int(input())
arr = list()
for _ in range(n):
    a, b = input().split()
    arr.append((int(a), b))

arr = sorted(arr, key=lambda x: x[0])

for i in arr:
    print(*i)
