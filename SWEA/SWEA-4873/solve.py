'''
시작시간: 15시 29분
종료시간: 15시 35분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    st = list(input())
    stack = []
    for i in st:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print('#{} {}'.format(tc, len(stack)))