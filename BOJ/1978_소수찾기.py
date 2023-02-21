# 난이도: 실버 5
# 알고리즘 유형:

"""
시작시간: 02:37
종료시간: 02:41
"""

n = int(input())
arr = list(map(int, input().split()))


# 소수 판별
def check_prime(num):
    sqrt_num = num ** (1 / 2)
    for i in range(2, int(sqrt_num + 1)):
        if num % i == 0:
            return False
    return True


# 하나씩 확인하며 1보다 크고 소수일 경우 카운트 추가
cnt = 0
for i in arr:
    if i > 1 and check_prime(i):
        cnt += 1

print(cnt)
