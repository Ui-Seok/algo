'''
시작시간: 22시 17분 -> 46qns~~~
종료시간: 시 분
'''

import sys
sys.stdin = open('input.txt', 'r')

# from collections import deque
t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    cheezes = list(map(int, input().split()))
    push = rotation = 0
    fire = {0:0, 1:0, 2:0, 3:0, 4:0}
    while True:
        i = 0
        if fire[i] == 0:
            fire[i] = cheezes.pop(0)
            fire[i] = fire[i] // 2
            i += 1
        if i > 4:
            i = 0