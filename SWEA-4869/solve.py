'''
시작시간: 22시 46분
종료시간: 
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

def get_tape(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return get_tape(n - 10) + (2 * get_tape(n - 20))

for tmp in range(t):
    n = int(input())
    answer = get_tape(n)
    print('#{} {}'.format(tmp + 1, answer))