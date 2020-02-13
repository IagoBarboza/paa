graph = {'a': ['b','c','d'], 'b': [], 'c': [], 'd': ['e'], 'e': []}
visited = []
queue = []

def bfs(graph, root):
  
  global visited
  global queue

  queue.append(root)
  
  while(len(queue) > 0):
    
    v = queue[0] #(I)
    
    visited.append(v) #(II)
    queue.pop(0) #(III)

    neighborhood = graph[v]
    
    for i in range(0, len(neighborhood)):
      if neighborhood[i] not in visited: queue.append(neighborhood[i]) #(IV)
    

bfs(graph, 'a')

print(visited)
print(queue)