# 난이도: 실버 1
# 알고리즘 유형:

"""
시작시간: 20:27
종료시간: 20:46
"""

n = int(input())

graph = list()
for _ in range(n):
    a = list(map(int, input()))
    graph.append(a)


def check_graph(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break
    if check == -1:
        print("(", end="")
        n = n // 2
        check_graph(x, y, n)  # 왼쪽 위
        check_graph(x, y + n, n)  # 오른쪽 위
        check_graph(x + n, y, n)  # 왼쪽 아래
        check_graph(x + n, y + n, n)  # 오른쪽 아래
        print(")", end="")
    elif check == 1:
        print(1, end="")
    else:
        print(0, end="")


check_graph(0, 0, n)
