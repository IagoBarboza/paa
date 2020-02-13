graph = {'a': ['b','c','d'], 'b': [], 'c': ['e'], 'd': [], 'e': []}
visited = []
stack = []

def dfs(graph, root):
  
  global visited
  global stack

  stack.append(root)
  
  while(len(stack) > 0):
    
    v = stack[len(stack)-1] #(I)
    
    visited.append(v) #(II)
    
    stack.pop() #(III)

    neighborhood = graph[v]
    
    for i in range(0, len(neighborhood)):
      if neighborhood[i] not in visited: stack.append(neighborhood[i]) #(IV)
    

dfs(graph, 'a')

print(visited)
print(stack)