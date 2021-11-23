#simple adjacency list
n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    u, v = map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)


for i, g in enumerate(graph):
    print(i, '->', g)