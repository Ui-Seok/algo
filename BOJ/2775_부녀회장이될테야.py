# 난이도: 브론즈 1
# 알고리즘 유형:

"""
시작시간:
종료시간:
"""


t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    answer = [i for i in range(1, n + 1)]

    for j in range(k):
        for k in range(1, n):
            answer[k] += answer[k - 1]

    print(answer[-1])
