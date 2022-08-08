import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True
    for i in linked_list[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    linked_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        linked_list[a].append(b)
        linked_list[b].append(a)

    visited = [False] * (N+1)
    parent = [0 for _ in range(N+1)]

    dfs(1)

    for i in range(2,N+1):
        print(parent[i])