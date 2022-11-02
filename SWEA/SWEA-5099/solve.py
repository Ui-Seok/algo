'''
시작시간: 20시 22분
종료시간: 시 분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    cheezes = list(map(int, input().split()))
    rotation = 1
    push = 0
    fire ={i:(0,0) for i in range(1, n + 1)}
    while push < m:
        if fire[rotation][1] == 0:
            fire[rotation] = (push + 1, cheezes[push])
            rotation += 1
            push += 1
            if rotation == n + 1:
                rotation = 1
        elif fire[rotation][1] != 0:
            fire[rotation] = (fire[rotation][0], fire[rotation][1] // 2)
            if fire[rotation][1] == 0:
                fire[rotation] = (push + 1, cheezes[push])
                push += 1
            rotation += 1
            if rotation == n + 1:
                rotation = 1
    count = []
    for i in range(1, n + 1):
        cnt = 0
        while fire[i][1] != 0:
            fire[i] = (fire[i][0], fire[i][1] // 2)
            cnt += 1
        count.append((fire[i][0], cnt))
    count = sorted(count, key = lambda x : (-x[1], -x[0]))
    print('#{} {}'.format(tc, count[0][0]))