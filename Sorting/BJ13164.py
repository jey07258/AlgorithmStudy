import sys

N, K = map(int, sys.stdin.readline().split())

height = list(map(int, sys.stdin.readline().split()))

distance = []

for i in range(N-1):
    distance.append((height[i+1] - height[i]))

distance.sort()

print(sum(distance[:(N-K)]))