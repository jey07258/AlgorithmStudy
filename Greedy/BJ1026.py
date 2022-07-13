N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

A.sort(reverse=True)
order = sorted(range(len(B)), key = lambda x: B[x])

for i in range(N):
    result += A[i] * B[order[i]]

print(result)