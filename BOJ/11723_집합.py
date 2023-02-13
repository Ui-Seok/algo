# 난이도: 실버 5
# 알고리즘 유형: 구현, 비트마스킹

"""
시작시간: 01:40
종료시간: 01:50
"""

# pypy3로 돌리면 메모리초과뜸!

import sys

input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    # 인풋이 하나일수도 있기 때문에 리스트로 받음
    x = list(input().split())
    # 수행 해야하는 부분을 받아옴
    a = x[0]

    # 해당 수행파트 시작
    if a == "add":
        # 리스트에 숫자가 없을때 리스트에 추가
        if int(x[1]) not in arr:
            arr.append(int(x[1]))

    elif a == "remove":
        # 리스트에 해당 숫자가 있을때 삭제
        if int(x[1]) in arr:
            arr.remove(int(x[1]))

    elif a == "check":
        # 해당 숫자가 있으면 1을 출력, 없으면 0을 출력
        if int(x[1]) in arr:
            print(1)
        else:
            print(0)

    elif a == "toggle":
        # 해당 숫자가 리스트에 있으면 삭제, 없으면 추가
        if int(x[1]) in arr:
            arr.remove(int(x[1]))
        else:
            arr.append(int(x[1]))

    elif a == "all":
        # 리스트를 1~20으로 변경
        arr = [i for i in range(1, 21)]

    elif a == "empty":
        # 리스트 초기화
        arr.clear()
