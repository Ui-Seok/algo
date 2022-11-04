n = int(input())
s = input()

cnt = 1

for idx in range(n-1):
	if s[idx] == s[idx+1]:
		continue
	else:
		cnt += 1

print(cnt)