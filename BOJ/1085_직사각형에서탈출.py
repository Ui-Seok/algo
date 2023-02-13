# 난이도: 브론즈 3
# 알고리즘 유형: 수학, 기하학

"""
시작시간: 22:38
종료시간: 22:42
"""

x, y, w, h = map(int, input().split())

min_x = min(x, w - x)
min_y = min(y, h - y)

print(min(min_x, min_y))
