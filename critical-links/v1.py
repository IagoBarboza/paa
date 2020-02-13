while(True):

  numberOfVertex = int(input())

  if (numberOfVertex == 0): 
    print('0 critical links')
    break

  g = [None]*numberOfVertex
  
  for j in range(0, numberOfVertex):
    i = input().split(" ")
    vIndex = int(i[0])
    i.pop(0)
    i.pop(0)
    vNeighbors = list(map(int, i))
    vNeighbors.sort()
    g[vIndex] = { 'd': None, 'l': None, 'neighbors': vNeighbors }

  input()

  rootVertex = 0

  for k in range (0, numberOfVertex):

    stack = []
    visited = []

    if rootVertex not in visited:
      
      stack.append(rootVertex)

      dCounter = 0

      criticalLinks = []

      while(len(stack) > 0):

        vIndex = stack[len(stack) - 1]
        
        v = g[vIndex]

        stack.pop()

        visited.append(vIndex)

        v['d'] = dCounter
        v['l'] = dCounter

        for i in range(0, len(v['neighbors'])):
          if v['neighbors'][i] not in visited: stack.append(v['neighbors'][i])

        dCounter += 1
      
    rootVertex += 1

  for i in range(0, len(g)):
    v = g[i]
    for j in range(0, len(v['neighbors'])):
      ni = v['neighbors'][j]
      n = g[ni]
      if (v['d'] < n['l']): criticalLinks.append(str(i)+' - '+str(ni))

  print(str(len(criticalLinks))+' critical links')
  print(criticalLinks)
