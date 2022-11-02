'''
시작시간: 19시 40분
종료시간: 19시 44분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    while m > 0:
        arr.append(arr.pop(0))
        m -= 1

    print('#{} {}'.format(tc, arr[0]))