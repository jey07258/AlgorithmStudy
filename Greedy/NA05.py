N, M = map(int, input().split())
W = list(map(int, input().split()))

k = 0
count = 0
while k < N:
    for i in range(k+1, N):
        if W[k] == W[i]:
            continue
        else:
            count += 1
    k += 1

print(count)