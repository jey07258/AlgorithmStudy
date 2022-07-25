# == BJ18406
import sys

N = list(map(int, sys.stdin.readline().rstrip()))
left, right = 0, 0

for i in range(len(N)//2):
    left += N[i]
    right += N[len(N)-(i+1)]

if left == right:
    print("LUCKY")
else:
    print("READY")