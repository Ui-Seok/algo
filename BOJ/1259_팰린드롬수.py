# 난이도: 브론즈 1
# 알고리즘 유형: 구현, 문자열

"""
시작시간: 02:30
종료시간: 02:42
"""

while True:
    a = list(input())
    if a == ["0"]:
        break

    # 길이가 홀수일 때
    if len(a) % 2:
        # 가운데 수를 빼고 양 옆으로 같은지 판별(우측은 역순으로 만들고 슬라이싱)
        if a[: len(a) // 2] == a[: len(a) // 2 : -1]:
            print("yes")
        else:
            print("no")

    # 길이가 짝수일 때
    else:
        # 절반을 기준으로 양 옆으로 같은지 판별(우측은 역순으로 만들고 슬라이싱)
        if a[: len(a) // 2] == a[: len(a) // 2 - 1 : -1]:
            print("yes")
        else:
            print("no")
