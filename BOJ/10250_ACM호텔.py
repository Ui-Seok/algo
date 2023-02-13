# 난이도: 브론즈 3
# 알고리즘 유형:

"""
시작시간: 04:10
종료시간: 04:18
"""

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    room = n // h

    if floor == 0:
        floor = h
    else:
        room += 1

    if room < 10:
        room = str(0) + str(room)
    else:
        room = str(room)

    ans = str(floor) + room
    print(ans)
