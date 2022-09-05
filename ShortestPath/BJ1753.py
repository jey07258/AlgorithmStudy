import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance, graph):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        this_dist, this_node = heapq.heappop(queue)

        for next_node, next_dist in graph[this_node]:
            if (this_dist + next_dist) < distance[next_node]:
                distance[next_node] = (this_dist + next_dist)
                heapq.heappush(queue, ((this_dist + next_dist), next_node))

if __name__ == '__main__':
    V, E = map(int, input().split())
    K = int(input())
    graph = [[] for _ in range(V+1)]
    distance = [INF] * (V+1)

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    dijkstra(K, distance, graph)

    for i in range(1, V+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])