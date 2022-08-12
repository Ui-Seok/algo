'''
시작시간: 11시 45분
종료시간: 11시 58분
'''
import sys
sys.stdin = open('input.txt', 'r')

for num in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = 0

    for i in range(2, n-1):
        have_light = buildings[(i - 2):(i + 3)]
        check_light = have_light.pop(2)
        high_building = max(have_light)
        if check_light > high_building:
            answer += check_light - high_building

    print(f'#{num} {answer}')