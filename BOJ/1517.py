'''
시작시간: 21시 14분
종료시간: 나중에 다시 풀어보기,,,, 아직 플레는 나에게 힘들다
'''

n = int(input())
arr = list(map(int, input().split()))

count = i = 0
stop = n - 1

def change(arr, i):
    global count, stop
    print(arr, stop)
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        count += 1
        i += 1
        if i == (n - 1):
            i = 0
            change(arr, i)
        else:
            change(arr, i)
    else:
        i += 1
        stop -= 1
        if stop == 0:
            return
        elif i == (n - 1):
            i = 0
            stop = n - 1
            change(arr, i)
        else: 
            change(arr, i)

change(arr, i)
print(count)
print(arr)