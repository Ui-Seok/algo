# 난이도: 실버 2
# 알고리즘 유형: 이분 탐색, 매개 변수 탐색

"""
시작시간: 12:20
종료시간: 12:43
"""

# 시간초과~
# k, n = map(int, input().split())
# length = [int(input()) for _ in range(k)]
# sum_leng = sum(length)
# max_leng = sum_leng // n

# while True:
#     cnt = 0
#     for i in length:
#         cnt += i // max_leng

#     if cnt >= n:
#         break
#     else:
#         max_leng -= 1

# print(max_leng)

# 이분탐색
k, n = map(int, input().split())
length = [int(input()) for i in range(k)]
start, end = 1, max(length)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in length:
        cnt += i // mid

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
