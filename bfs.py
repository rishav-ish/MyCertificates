from collections import deque

#BFS implementation

#lets get the graph from user
#undirected graph
from typing import Collection


n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    u, v = map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)


for i, g in enumerate(graph):
    print(i, '->',g)

#lets implement BFS here

visited = [False] * (n+1)
print(len(visited))
res = []

for node in range(1,n+1):
    if not visited[node]:
        q = deque([node])
        visited[node] = True

        while q:
            temp = q.popleft()
            res.append(temp)

            for adj in graph[temp]:
                if not visited[adj]:
                    visited[adj] = True
                    q.append(adj)


print(res)
