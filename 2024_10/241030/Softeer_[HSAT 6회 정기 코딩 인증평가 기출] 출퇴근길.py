import sys
sys.setrecursionlimit(10**8)
from collections import deque

n, m  = map(int, sys.stdin.readline().split())

go_graph = [[] for _ in range(n + 1)]
back_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    go_graph[x].append(y)
    back_graph[y].append(x)

S, T = map(int, sys.stdin.readline().split())

def bfs(graph, current, visited):
    q = deque([current])

    visited[current] = 1

    while q:
        x = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)

# def dfs(graph, current, visited):
#     if visited[current] == 1:
#         return
#     else:
#         visited[current] = 1
#         for node in graph[current]:
#             dfs(graph, node, visited)

#     return

fromS, fromT, toS, toT = [[0] * (n+1) for _ in range(4)]
fromS[T] = fromT[S] = 1

bfs(go_graph, S, fromS)
bfs(go_graph, T, fromT)
bfs(back_graph, S, toS)
bfs(back_graph, T, toT)

cnt = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt += 1
print(cnt - 2)