#take input from user
v, e = map(int, input().split())

graph = [[] for i in range(v+1)]

#undirected graph
for _ in range(e):
    src, dest = map(int, input().split())

    graph[src].append(dest)
    graph[dest].append(src)

visited = [False] * (v+1)
res = []


for i in range(1,v+1):
    stack = [i]

    while stack:
        temp = stack.pop()

        if visited[temp]:
            continue

        res.append(temp)
        visited[temp] = True

        for adj in graph[temp]:
            stack.append(adj)


print(res)