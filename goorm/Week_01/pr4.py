n = int(input())
arr = list(map(int, input().split()))
prime_list = list()

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

for num in range(2, n+1):
    if is_prime(num):
        prime_list.append(num)

answer = 0
for idx in prime_list:
    answer += arr[idx-1]
print(answer)