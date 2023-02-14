# 난이도: 실버 5
# 알고리즘 유형: 문자열, 정렬

"""
시작시간: 01:58
종료시간: 02:29
"""

n = int(input())

# key=문자, value=해당 문자열의 길이
arr = dict()
for _ in range(n):
    a = input()
    arr[a] = len(a)

# 길이를 바탕으로 먼저 정렬하고, 사전순으로 정렬
arr = sorted(arr.items(), key=lambda x: (x[1], x[0]))

# key값만 출력
for k in arr:
    print(k[0])
