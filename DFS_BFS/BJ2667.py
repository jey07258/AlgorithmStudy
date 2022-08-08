import sys

def dfs(x, y):
    if (x < 0) or (x >= N) or (y < 0) or (y >= N):
        return False

    if field[x][y] == 1:
        global count
        count += 1
        field[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    field = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    visited = [[False] * N for _ in range(N)]
    count = 0
    result = 0
    size = []    

    for i in range(N):
        for j in range(N):
            if dfs(i, j) == True:
                result += 1
                size.append(count)
                count = 0

    size.sort()
    print(result)
    for i in range(len(size)):
        print(size[i])