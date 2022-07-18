N = int(input())
S = list(map(int, input().split()))
S.sort()

result = 1

for x in S:
    if result < x:
        break
    result += x

print(result)