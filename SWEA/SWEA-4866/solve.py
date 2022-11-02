'''
시작시간: 23시 19분
종료시간: 24시 33분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tmp in range(1, t + 1):
    arr = list(input()) # 리스트로 받기
    stack_list = [] # 스택 리스트 만들기
    answer = 1
    for i in arr:   # 리스트 인자 하나씩 보기
        if i == '(' or i == '{':
            stack_list.append(i)
            continue
        # 리스트 마지막이 알맞은 괄호일때 마지막 제거하기
        if i == ')' or i == '}':
            if not stack_list:
                answer = 0
                break
            elif i == ')':
                if stack_list.pop() == '{':
                    answer = 0
                    break
            elif i == '}':
                if stack_list.pop() == '(':
                    answer = 0
                    break
    if stack_list:
        answer = 0
        print(f'#{tmp} {answer}')
    else:
        print(f'#{tmp} {answer}')