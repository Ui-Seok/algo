# 난이도: 브론즈 1
# 알고리즘 유형: 수학, 구현, 조합론

"""
시작시간: 01:18
종료시간: 01:21
"""

n, k = map(int, input().split())

pac_n = 1
for i in range(1, n + 1):
    pac_n *= i

pac_k = 1
for j in range(1, k + 1):
    pac_k *= j

pac_n_k = 1
for k in range(1, n - k + 1):
    pac_n_k *= k

print(pac_n // (pac_k * pac_n_k))
