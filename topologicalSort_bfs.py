import collections

#kahn's algorithm

v,e = map(int ,input().split())

graph = [[] for _ in range(v)]

for _ in range(e):
    src, dest = map(int, input().split())
    graph[src].append(dest)


#implementing kahn's algorithm here...
#lets find in degree
in_degress = [0] * v

for i in range(v):
    for n in graph[i]:
        in_degress[n] += 1


#here put node in queque whose value is 0 in in_degress array
q = collections.deque([])

for i, val in enumerate(in_degress):
    if val == 0:
        q.append(i)

res = []  #will be storing result here...
#lets implement bfs here

while q:
    temp = q.popleft()

    res.append(temp)

    for t in graph[temp]:
        in_degress[t] -= 1
        if in_degress[t] == 0:
            q.append(t)


print(res)