'''
시작시간: 14시 59분
종료시간: 15시 2분
'''

import sys
sys.stdin = open('input.txt', 'r')

def get_max(x):
    max_num = -1
    for i in x:
        if max_num < i:
            max_num = i
    return max_num

def get_min(x):
    min_num = 987654321
    for i in x:
        if min_num > i:
            min_num = i
    return min_num

t = int(input())
for tmp in range(t):
    n = int(input())
    case = list(map(int, input().split()))
    answer = get_max(case) - get_min(case)

    print(f'#{tmp+1} {answer}')