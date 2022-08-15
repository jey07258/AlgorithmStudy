import sys

N = int(sys.stdin.readline())

array = []
for _ in range(N):
    temp = sys.stdin.readline().split()
    array.append((temp[0], int(temp[1])))

array = sorted(array, key=lambda k: k[1])

for k in array:
    print(k[0], end=' ')