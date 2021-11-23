'''
    We will be usig kahns algorithm
    if the array count generated equal to node count in graph
    We will return True
    else return False
'''

import collections

#lets take graph from user
v, e = map(int, input().split())

graph = [[] for _ in range(v+1)] #1 based indexing DAG Graph

for _ in range(e):
    src, dest = map(int, input().split())
    graph[src].append(dest)


in_degress = [0]*(v+1)

for i in range(1,v+1):
    for t in graph[i]:
        in_degress[t] += 1


q = collections.deque([])

for i, val in enumerate(in_degress):
    if val == 0:
        q.append(i)

count = 0
while q:
    temp = q.popleft()
    count += 1

    for t in graph[temp]:
        in_degress[t] -= 1
        if in_degress[t] == 0:
            q.append(t)


if count == v+1:
    print('False')
else:
    print('True')