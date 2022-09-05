import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, time, graph):
    queue = []
    heapq.heappush(queue, (0, start))
    time[start] = 0

    while queue:
        this_time, this_node = heapq.heappop(queue)

        for next_node, next_time in graph[this_node]:
            if (this_time + next_time) < time[next_node]:
                time[next_node] = (this_time + next_time)
                heapq.heappush(queue, ((this_time + next_time), next_node))

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, d, c = map(int, input().split())

        graph = [[] for _ in range(n+1)]
        time = [INF] * (n+1)

        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))

        dijkstra(c, time, graph)

        count = 0
        answer = 0
        for i in time:
            if i != INF:
                count += 1
                answer = max(answer, i)
        
        print(f"{count} {answer}")