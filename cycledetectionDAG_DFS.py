#lets take graph from user
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    src, dest = map(int, input().split())

    graph[src].append(dest)


visited = [False] * (v+1)
dfs_visited = [False] * (v+1)

def checkCycle(i):
    visited[i] = True
    dfs_visited[i] = True

    for n in graph[i]:
        if not visited[i]:
            if checkCycle(n):
                return True

        elif dfs_visited[i]:
            return True

    dfs_visited[i] = False
    return False

for i in range(1, v+1):
    if checkCycle(i):
        print(True)
        break


print('IF True not printed it means there will be no cycle')