import sys
sys.setrecursionlimit(10**4)

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if field[nx][ny] == 1:
                field[nx][ny] = -1
                dfs(nx, ny)
    

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        
        field = [[0] * M for _ in range(N)]
        for _ in range(K):
            y, x = map(int, sys.stdin.readline().split())
            field[x][y] = 1

        count = 0

        for i in range(N):
            for j in range(M):
                if field[i][j] > 0:
                    dfs(i, j)
                    count += 1

        print(count)