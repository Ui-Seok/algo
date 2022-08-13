'''
시작시간: 16시 25분
종료시간: 17시 15분
'''

n = int(input())
row = [0] * n
answer = 0

def fine_node(x):
    for i in range(x):
        if (row[x] == row[i]) or (abs(row[x] - row[i]) == abs(x - i)):
            return False
    return True

def n_queens(x):
    global answer
    if x == n:
        answer += 1
        return
    
    else:
        for i in range(n):
            row[x] = i
            if fine_node(x):
                n_queens(x + 1)
n_queens(0)
print(answer)