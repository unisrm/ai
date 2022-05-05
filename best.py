from queue import PriorityQueue
v = 8
graph = [[] for i in range(v)]
def best_first_search(source, target, n):
  visited = [0] * n
  visited[0] = True
  pq = PriorityQueue()
  pq.put((0, source))
  while pq.empty() == False:
    u = pq.get()[1]
    print(u, end=" ")
    if u == target:
      break
    for v, c in graph[u]:
      if visited[v] == False:
        visited[v] = True
        pq.put((c, v))
  print()
def addedge(x, y, cost):
  graph[x].append((y, cost))
  graph[y].append((x, cost))
addedge(0, 5, 3)
addedge(5, 6, 2)
addedge(6, 7, 9)
addedge(7, 4, 1)
addedge(0, 1, 5)
addedge(0, 2, 1)
addedge(2, 3, 2)
addedge(1, 4, 1)
addedge(3, 4, 2)

source = int(input('Enter the start node:-'))
target = int(input('Enter the goal node:-'))

print("path till goal node is : - ")
best_first_search(source, target, v)
