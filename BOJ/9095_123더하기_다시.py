# 난이도: 실버 3
# 알고리즘 유형: DP

"""
시작시간: 02:30
종료시간: 02:54
"""

t = int(input())

arr = [0 for _ in range(11)]
arr[1] = 1  # 1
arr[2] = 2  # 1+1, 2
arr[3] = 4  # 1+1+1, 1+2, 2+1, 3

for i in range(4, 11):
    arr[i] = sum(arr[i - 3 : i])

for _ in range(t):
    n = int(input())
    print(arr[n])
