'''
시작시간: 17시 15분
종료시간: 17시 34분
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tmp in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    new_arr = []
    for i in range(n//2):
        new_arr.append(arr[i])
        new_arr.append(arr[-(i+1)])
    pr_list = ' '.join(map(str, new_arr[:10]))
    print('#{} {}'.format(tmp + 1, pr_list))