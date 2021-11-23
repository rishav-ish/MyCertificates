import collections


#toplogical sort is perform for DAG Graph 

#lets take input from user
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    src, dest = map(int, input().split())

    graph[src].append(dest)


visited = [False] * (v+1)
stack = collections.deque([])

def dfs(node):
    visited[node] = True

    for n in graph[node]:
        if not visited[n]:
            dfs(n)

    stack.append(node)

for i in range(1,v+1):
    if not visited[i]:
        dfs(i)


res = []
while stack:
    res.append(stack.pop())

print(res)

