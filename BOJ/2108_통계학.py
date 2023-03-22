# 난이도: 실버 3
# 알고리즘 유형: 수학, 구현, 정렬

"""
시작시간: 13:16
종료시간: 13:43
"""

n = int(input())
arr = [int(input()) for _ in range(n)]


# 산술평균 구하기
def get_avg(arr):
    return round(sum(arr) / n)


# 중앙값 구하기
def get_med(arr):
    arr = sorted(arr)
    med = len(arr) // 2
    return arr[med]


# 최빈값 구하기 - 딕셔너리 형태로 key는 주어진 숫자, value는 나온 횟수를 기준으로 하여 만들기
def get_most(arr):
    check_dict = dict()
    for i in arr:
        if check_dict.get(i):
            check_dict[i] += 1
        else:
            check_dict[i] = 1
    # 가장 많이 나온것을 기준으로 정렬, key를 오름차순으로 정렬
    check_dict = sorted(check_dict.items(), key=lambda x: (-x[1], x[0]))
    max_cnt = check_dict[0][1]
    tmp = list()
    # 가장 많이 나온 숫자만 확인하여 새로운 리스트에 추가
    for i, j in check_dict:
        if j == max_cnt:
            tmp.append(i)
    # 두 번째로 작은 원소이므로 index를 1로 하고 만약 한개의 원소만 존재하면 첫 번째 출력
    return tmp[1] if len(tmp) > 1 else tmp[0]


# 범위 구하기
def get_range(arr):
    return max(arr) - min(arr)


print(get_avg(arr))
print(get_med(arr))
print(get_most(arr))
print(get_range(arr))
