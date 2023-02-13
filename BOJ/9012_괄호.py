# 난이도: 실버 4
# 알고리즘 유형: 자료구조, 문자열, 스택

"""
시작시간: 00:49
종료시간: 00:56
"""

t = int(input())
for _ in range(t):
    td = list(input())
    ans = "YES"

    if td[-1] == "(":
        ans = "NO"
    else:
        cnt_l = 0
        cnt_r = 0
        for i in td:
            if i == "(":
                cnt_l += 1
            else:
                cnt_r += 1
            if cnt_r > cnt_l:
                ans = "NO"
                break
        if cnt_l != cnt_r:
            ans = "NO"
    print(ans)
