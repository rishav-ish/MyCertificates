import collections

#lets get graph from user
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    src, dest = map(int, input().split())

    graph[src].append(dest)
    graph[dest].append(src)


#lets check bipartite here...
colors = [-1] * (v+1)   #by default nothing is colored; -1 shows nothing is color


def checkBipartite(node):
    colors[node] = 1    #lets start coloring with 1
    q = collections.deque([node])

    while q:
        temp = q.popleft()

        for t in graph[temp]:
            if colors[t] == -1:
                colors[t] = 1 - colors[temp]
                q.append(t)

            elif colors[t] == colors[temp]:
                return False

    return True


for i in range(1, v+1):
    if colors[i] == -1:
        if not checkBipartite(i):
            print(False)
            break

    
print('If false is not printed it means the graph is bipartite')

