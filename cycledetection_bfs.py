#lets take graph from undirected graph from user
from collections import deque
import collections

def isCycle(n, visited):
    visited[n] = True
    q = collections.deque([(n,-1)])

    while q:
        node, parent = q.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i,node))
            else:
                if i != parent:
                    return True

    return False


v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    src, dest = map(int, input().split())

    graph[src].append(dest)
    graph[dest].append(src)


visited = [False] * (v+1)

for i in range(1, v+1):
    if not visited[i]:
        if isCycle(i, visited):
            print(True)


print(visited)




