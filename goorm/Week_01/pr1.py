n = int(input())
bridge = list(map(int, input().split()))

answer = 1
for br in bridge:
    answer *= br
print(answer)