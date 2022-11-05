n = int(input())
s = list(input())

phone = {'1': ['1', '.', ',', '?', '!'],
		 '2': ['2', 'A', 'B', 'C'],
		 '3': ['3', 'D', 'E', 'F'],
		 '4': ['4', 'G', 'H', 'I'],
		 '5': ['5', 'J', 'K', 'L'],
		 '6': ['6', 'M', 'N', 'O'],
		 '7': ['7', 'P', 'Q', 'R', 'S'],
		 '8': ['8', 'T', 'U', 'V'],
		 '9': ['9', 'W', 'X', 'Y', 'Z']}

start = s[0]
cnt = 0
answer = ''

for i in range(n):
	if start == s[i]:
		cnt += 1
	else:
		if start == '1' or start == '7' or start == '9':
			cnt = cnt % 5
			if cnt == 0:
				cnt = 5
		else:
			cnt = cnt % 4
			if cnt == 0:
				cnt = 4
				
		answer += phone[start][cnt-1]
		start = s[i]
		cnt = 1

if start == '1' or start == '7' or start == '9':
	cnt = cnt % 5
	if cnt == 0:
		cnt = 5
else:
	cnt = cnt % 4
	if cnt == 0:
		cnt = 4
				
answer += phone[start][cnt-1]

print(answer)