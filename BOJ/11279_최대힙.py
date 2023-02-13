# 난이도: 실버 2
# 알고리즘 유형: 자료구조, 큐

"""
시작시간: 02:08
종료시간: 02:15
"""

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())

# 인풋이 들어오는 원소들을 담기위한 리스트 생성
arr = list()

for _ in range(n):
    a = int(input())
    if a == 0:
        # 리스트에 원소가 있을 때
        if arr:
            max_num = heappop(arr)
            print(-max_num)
        # 리스트에 원소가 없을 때
        else:
            print(0)
    else:
        heappush(arr, -a)
