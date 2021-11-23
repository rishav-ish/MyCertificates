#take graph input from user
def dfs(vertex, visited, res):
    res.append(vertex)
    visited[vertex] = True

    for adj in graph[vertex]:
        if not visited[adj]:
            dfs(adj,visited,res)


v, e = map(int,input().split())

graph = [[] for i in range(v+1)]


#undirected graph
for _ in range(e):
    src, dest = map(int,input().split())

    graph[src].append(dest)
    graph[dest].append(src)


visited = [False] * (v+1)
res = []

for i in range(1,v+1):
    if not visited[i]:
        dfs(i,visited,res)


print(res)
