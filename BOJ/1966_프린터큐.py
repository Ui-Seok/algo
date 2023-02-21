# 난이도: 실버 3
# 알고리즘 유형: 구현, 자료구조, 큐, 시뮬레이션

"""
시작시간: 02:05
종료시간: 다시 풀기
"""

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    queue_arr = list(map(int, input().split()))
    idx_arr = list(range(n))
    idx_arr[m] = "answer"

    cnt = 0
    while True:
        if queue_arr[0] == max(queue_arr):
            cnt += 1

            if idx_arr[0] == "answer":
                print(cnt)
                break

            else:
                del queue_arr[0]
                del idx_arr[0]

        else:
            queue_arr.append(queue_arr.pop(0))
            idx_arr.append(idx_arr.pop(0))
