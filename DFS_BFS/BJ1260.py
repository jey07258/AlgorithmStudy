import sys
from collections import deque

def dfs(node, visited):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i, visited)

def bfs(node, visited):
    queue = deque([node])
    visited[node] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__ == '__main__':
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(len(graph)):
        graph[i].sort()

    dfs_visited = [False] * (N+1)
    bfs_visited = [False] * (N+1)

    dfs(V, dfs_visited)
    print()
    bfs(V, bfs_visited)