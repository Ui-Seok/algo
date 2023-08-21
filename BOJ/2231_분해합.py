# 난이도: 브론즈 2
# 알고리즘 유형: 브루투포스

"""
시작시간: 20:18
종료시간:
"""

n = int(input())

for i in range(1, n + 1):
    num = sum(map(int, str(i)))
    num_sum = i + num

    if num_sum == n:
        print(i)
        break
else:
    print(0)
