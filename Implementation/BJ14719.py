import sys
H, W = map(int, input().split())
blo = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
for i in range(1,W-1):
    left = max(blo[:i])
    right = max(blo[i+1:])
    if blo[i] >= left or blo[i] >= right:
        continue
    if left <= right:
        result += left - blo[i]
    else:
        result += right - blo[i]

print(result)