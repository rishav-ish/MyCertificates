#lets take graph
from collections import deque

def isCycle(node, parent, visited):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            if isCycle(i,node,visited):
                return True
        elif i != parent:
            return True

    return False



v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    src, dest = map(int,input().split())

    graph[src].append(dest)
    graph[dest].append(src)


#lets check for cycle here
visited = [False] * (v+1)

for i in range(1, v+1):
    if not visited[i]:
        if isCycle(i,-1,visited):
            print(True)


