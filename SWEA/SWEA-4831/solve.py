'''
시작시간: 15시 10분
종료시간: 
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tmp in range(1, t + 1):
    # k=최대 이동가능 정류장수, n=종점, m=충전기가 설치된 정류장 개수
    k, n, m = map(int, input().split())
    charges = list(map(int, input().split()))
    bus_stop = [0] * (n + 1)
    br = 1  # break point 설정
    for charge in charges:
        bus_stop[charge] += 1
    for i in range(m-1):
        diff = charges[i + 1] - charges[i]
        if diff > k:
            print(f'#{tmp}', 0)
            br = 0  # 밑의 while문 돌지않게 하기 위해 0으로 설정
            continue
    cnt = 0
    i = 1 + k
    while br:
        if bus_stop[i] == 1:
            cnt += 1
            i += k
            if i >= n:
                print(f'#{tmp} {cnt}')
                break
        else:
            i -= 1