# 난이도: 브론즈 1
# 알고리즘 유형: 수학, 정수론, 유클리즈호제법

"""
시작시간: 23:15
종료시간: 23:22
"""

a, b = map(int, input().split())

# --최대공약수 구하기
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# --최소공배수 구하기
for i in range(max(a, b), (a * b) + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break
