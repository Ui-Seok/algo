# 난이도: 실버 4
# 알고리즘 유형: 자료구조, 정렬, 이분탐색

"""
시작시간: 02:32
종료시간: 02:41
"""

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
check_arr = list(map(int, input().split()))

# 리스트 정렬
arr.sort()


# 이진탐색 함수 코드
def binary_search(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr, start, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, end, target)


# 확인해야할 리스트에서 하나씩 꺼내가며 이진탐색으로 확인
for i in check_arr:
    target = binary_search(arr, 0, n - 1, i)
    if target == i:
        print(1)
    else:
        print(0)
