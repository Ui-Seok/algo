'''
시작시간: 18시 5분
종료시간: 18시 18분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tmp in range(t):
    str1 = input()
    str2 = input()
    if (str1 in str2):
        print('#{} 1'.format(tmp + 1))
    else: print('#{} 0'.format(tmp + 1))