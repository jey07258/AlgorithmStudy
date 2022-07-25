N, M = map(int, input().split())
x, y, direction = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
field[x][y] = 1
count = 1
direction_count = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    direction -= 1
    if direction == -1:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    if field[nx][ny] == 0:
        x, y = nx, ny
        field[nx][ny] = 1
        count += 1
        direction_count = 0
    else:
        direction_count += 1

    if direction_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if field[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        direction_count = 0

print(count)