'''
시작시간: 14시 00분
종료시간: 14시 22분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

def DFS(arr, check, start):
        global answer
        check[start] = True
        if check[g] == True:
            answer = 1
            return answer
        for i in arr[start]:
            if check[(i - 1)] == False:
                DFS(arr, check, (i - 1))
            else:
                continue

for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v)]
    check = [False] * v
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a - 1].append(b)
    s, g = map(int, input().split())
    s -= 1; g -= 1
    answer = 0
    DFS(arr, check, s)
    print('#{} {}'.format(tc, answer))