from collections import deque
import sys

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<N) and (0<=ny<M) and field[nx][ny]==0:
                field[nx][ny] = field[x][y] + 1
                queue.append([nx, ny])

if __name__ == '__main__':
    M, N = map(int, input().split())
    field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([])
    count = 0

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                queue.append([i, j])

    bfs()

    for i in field:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        count = max(count, max(i))

    print(count - 1)