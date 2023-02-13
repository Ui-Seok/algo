# 난이도: 골드 4
# 알고리즘 유형: 자료구조, 그래프, 분리집합

"""
시작시간: 01:15
종료시간: 02:00
"""

# n, m = map(int, input().split())
# know_arr = list(map(int, input().split()))

# check = [False for _ in range(n+1)]
# # 파티의 개수
# cnt = 0

# # 진실을 알고있는 사람이 있을경우 해당 번호를 True로 변경
# if know_arr[0] != 0:
#     for i in list(know_arr[1:]):
#         check[i] = True

# party_people = list()
# # 진실을 알고있는 사람 체크
# for _ in range(m):
#     party_arr = list(map(int, input().split()))
#     nums = party_arr[0]
#     people = list(party_arr[1:])
#     party_people.append((nums, people))

#     # 파티에 참석한 사람들을 확인하며 진실을 알고있는 사람이 존재하면 전부 진실로 변경
#     for i in people:
#         if check[i]:
#             for i in people:
#                 check[i]  = True
#             break

# # 과장 할 수 있는 파티의 개수 찾기
# # 파티에 참석한 사람들을 확인하며 전부 False로 이루어진 파티일 경우 추가
# for k, v in party_people:
#     for p in v:
#         if check[p]:
#             break
#     else:
#         cnt += 1

# print(cnt)


from collections import deque

n, m = map(int, input().split())
know_arr = list(map(int, input().split()))

# bfs로 풀기위한 딕셔너리 map 생성 (양방향), 파티정보를 담을 리스트 생성
maps = {i: list() for i in range(1, n + 1)}
party_info = list()
for _ in range(m):
    p_list = list(map(int, input().split()))
    pp = p_list[0]  # 파티에 있는 사람 수
    pn = p_list[1:]  # 파티에 참석한 사람의 번호
    party_info.append((pp, pn))  # 파티의 정보 담기

    for i in pn:
        maps[i] += pn

# maps에 중복으로 들어간 인자들 삭제
for i in range(1, n + 1):
    maps[i] = list(set(maps[i]))

# 큐 생성 및 진실을 알고있는 사람 확인
if know_arr[0] == 0:
    print(m)
else:
    q = deque()
    check = [False for _ in range(n + 1)]
    true_p = know_arr[1:]

    # 진실을 알고있는 사람을 큐에 넣고 True로 변경
    for p in true_p:
        q.append(p)
        check[p] = True

    while q:
        a = q.popleft()
        for x in maps[a]:
            if not check[x]:
                check[x] = True
                q.append(x)

    # 과장을 할 수 있는 파티 확인
    answer = 0
    for k, v in party_info:
        if check[v[0]]:
            continue
        else:
            answer += 1
    print(answer)
