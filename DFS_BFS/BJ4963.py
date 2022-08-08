from collections import deque
import sys

def bfs(i, j):
    queue = deque([])
    queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<h) and (0<=ny<w) and field[nx][ny]==1:
                field[nx][ny] = 0
                queue.append([nx, ny])


if __name__ == '__main__':
    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]

    while True:
        count = 0
        w, h = map(int, input().split())
        if (w==0) and (h==0):
            break
        field = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if field[i][j] == 1:
                    bfs(i, j)
                    count += 1
        print(count)