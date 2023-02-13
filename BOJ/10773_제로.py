# 난이도: 실버 4
# 알고리즘 유형: 구현, 자료구조, 스택

"""
시작시간: 02:38
종료시간: 02:40
"""

import sys

input = sys.stdin.readline

k = int(input())
arr = list()

for _ in range(k):
    a = int(input())
    if a == 0:
        del arr[-1]
    else:
        arr.append(a)

print(sum(arr))
