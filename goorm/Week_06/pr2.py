n = int(input())
s = input()

answer = ""
for i in range(0, n - 1, 2):
    a = ord(s[i]) - 97
    a += int(s[i + 1]) ** 2

    if a > 25:
        a = a % 26

    answer += chr(a + 97)

print(answer)
