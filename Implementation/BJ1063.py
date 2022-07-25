import sys

k_first, s_first, N = input().split()
kx, ky = (ord(k_first[0]) - 64), int(k_first[1])
sx, sy = (ord(s_first[0]) - 64), int(s_first[1])
N = int(N)

moving = [sys.stdin.readline().strip() for _ in range(N)]

move_types = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

for m in moving:
    for i in range(len(move_types)):
        if m == move_types[i]:
            nkx = kx + dx[i]
            nky = ky + dy[i]
            if nkx == sx and nky == sy:
                nsx = sx + dx[i]
                nsy = sy + dy[i]
            else:
                nsx = sx
                nsy = sy
    if (nkx < 1) or (nky < 1) or (nkx > 8) or (nky > 8) or (nsx < 1) or (nsy < 1) or (nsx > 8) or (nsy > 8):
        continue

    kx, ky, sx, sy = nkx, nky, nsx, nsy

k_final = chr(kx+64)+str(ky)
s_final = chr(sx+64)+str(sy)

print(k_final)
print(s_final)