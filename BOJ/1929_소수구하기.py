# 난이도: 실버 3
# 알고리즘 유형: 수학, 정수론, 소수 판정, 에라토스테네스의 체

"""
시작시간: 03:20
종료시간: 03:42
"""

m, n = map(int, input().split())


# 소수 판별 코드
def check_prime(num):
    root = int(num ** (1 / 2))
    for i in range(2, root + 1):
        if num % i == 0:
            return False
    return True


for i in range(m, n + 1):
    if i == 1:
        continue
    if check_prime(i):
        print(i)
