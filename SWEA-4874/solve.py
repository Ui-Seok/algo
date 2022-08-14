'''
시작시간: 16시 53분
종료시간: 17시 21분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    arr = list(map(str, input().split()))
    stack = []
    calc = ['+', '-', '*', '/']
    answer = 0
    for ar in arr:
        if ar == '.':
            if len(stack) > 2:
                answer = 'error'
                break
            else:
                answer += int(stack[0])
                break
        if not ar in calc:
            stack.append(int(ar))
        elif ar in calc:
            if len(stack) < 2:
                answer = 'error'
                break
            if ar == '+':
                stack.append(stack.pop(-2) + stack.pop())
            elif ar == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif ar == '*':
                stack.append(stack.pop(-2) * stack.pop())
            elif ar == '/':
                stack.append(stack.pop(-2) // stack.pop())

    print('#{} {}'.format(tc, answer))