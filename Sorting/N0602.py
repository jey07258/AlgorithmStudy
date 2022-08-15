import sys

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline().strip()) for _ in range(N)]

num = sorted(num, reverse=True)

print(num)