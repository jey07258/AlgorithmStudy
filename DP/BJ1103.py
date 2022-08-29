import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global check
    if not((0 <= x < N) and (0 <= y < M)) or (field[x][y] == "H"):
        return 0
    if visited[x][y]:
        check = True
        return -1
    if dp[x][y] != -1:
        return dp[x][y]

    visited[x][y] = True
    for i in range(4):
        nx = x + (dx[i] * int(field[x][y]))
        ny = y + (dy[i] * int(field[x][y]))     
        dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
        if check:
            return -1       
    visited[x][y] = False

    return dp[x][y]      

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    field = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    visited = [[False] * M for _ in range(N)]
    dp = [[-1] * M for _ in range(N)]
    check = False

    print(dfs(0,0))