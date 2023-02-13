# 난이도: 실버 5
# 알고리즘 유형: 정렬

"""
시작시간: 03:46
종료시간: 03:52
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = list()
# 빈 리스트에 x, y 좌표를 묶어서 추가함
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

# 먼저 y좌표를 오름차순으로 정렬한 후 x좌표를 오름차순으로 정렬함
arr = sorted(arr, key=lambda x: (x[1], x[0]))

# 0번째 인덱스부터 하나씩 출력
for i in range(n):
    print(*arr[i])
