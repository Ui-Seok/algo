# 난이도: 실버 4
# 알고리즘 유형: 브루트포스

"""
시작시간: 21:36
종료시간: 다시풀기
"""

n, m = map(int, input().split())
board = list()
for _ in range(n):
    board.append(list(input()))

change_count = 64
for i in range(n - 7):
    for j in range(m - 7):
        cnt = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if x % 2 == 0 and y % 2 == 0:
                    if board[x][y] == "W":
                        cnt += 1
                elif x % 2 == 0 and y % 2 == 1:
                    if board[x][y] == "B":
                        cnt += 1
                elif x % 2 == 1 and y % 2 == 0:
                    if board[x][y] == "B":
                        cnt += 1
                elif x % 2 == 1 and y % 2 == 1:
                    if board[x][y] == "W":
                        cnt += 1
        if min(cnt, 64 - cnt) < change_count:
            change_count = min(cnt, 64 - cnt)

print(change_count)
