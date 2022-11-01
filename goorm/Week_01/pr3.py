distance = list(map(int, input().split()))
distance.sort()

print(distance[3] - distance[0] + distance[2] - distance[1])