# 난이도: 실버 2
# 알고리즘 유형: 자료구조, 스택

"""
시작시간: 03:07
종료시간: 03:25
"""

n = int(input())
# 정답 체크 리스트
check_arr = [int(input()) for _ in range(n)]
# 쌓을 리스트
stack_arr = [0]
# push, pop을 기록할 리스트
answer = list()

# 체크 리스트 index 확인, stack 리스트에 넣을 숫자
idx, st_num = 0, 1
# 인덱스가 n미만, 넣을 숫자는 n이하
while idx < n and st_num <= n + 1:
    # 체크 리스트 index와 stack 리스트 마지막이 다르면 숫자를 넣고 1추가, push를 기록
    if stack_arr[-1] != check_arr[idx]:
        stack_arr.append(st_num)
        st_num += 1
        answer.append("+")
    # 체크 리스트 index와 stack 리스트 마지막이 같으면 숫자 뽑고 index 1추가, pop을 기록
    else:
        stack_arr.pop()
        idx += 1
        answer.append("-")

if stack_arr != [0]:
    print("NO")
else:
    for i in answer:
        print(*i)
