N = int(input())
T = list(map(int, input().split()))
T.sort()
result = 0

for i in range(N):
    result += T[i]*(N-i)

print(result)