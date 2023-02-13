# 난이도: 브론즈 2
# 알고리즘 유형: 브루트포스

"""
시작시간: 02:49
종료시간: 02:59
"""

from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

comb_list = combinations(arr, 3)

max_num = 0
for i in comb_list:
    num = sum(i)

    if num == m:
        max_num = num
        break
    else:
        if num <= m and num > max_num:
            max_num = num

print(max_num)
