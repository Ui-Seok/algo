'''
시작시간: 15시 47분
종료시간: 16시 7분
힌트보고 품
'''
import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
a = [i for i in range(1, 13)]
def counting(num, x):
    cnt = 0
    while x > 0:
        cnt += x % 2
        x = x // 2
    if cnt == num:
        return True
    else: return False

for tmp in range(t):
    answer = 0
    n, k = map(int, input().split())
    for i in range(1<<12):
        if counting(n, i):
            check = 0
            for j in range(12):
                if i & (1<<j):
                    check += j + 1
            if check == k:
                answer += 1
    print('#{} {}'.format(tmp + 1, answer))