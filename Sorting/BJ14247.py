import sys

N = int(sys.stdin.readline())

Hi = list(map(int, sys.stdin.readline().split()))
Ai = list(map(int, sys.stdin.readline().split()))

tree = []

for i in range(N):
    tree.append((Hi[i], Ai[i]))

tree = sorted(tree, key=lambda k: k[1])

result = 0
for i in range(N):
    result += tree[i][0] + tree[i][1] * i

print(result)