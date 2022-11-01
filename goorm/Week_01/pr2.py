n, s = list(map(str, input().split()))
name_list = [input() for _ in range(n)]

cnt = 0
for name in name_list:
    if s in name:
        cnt += 1
print(cnt)