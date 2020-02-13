while(True):

  V = int(input())

  if (V == 0):
    print('0 critical links')
    break

  g = [None]*V

  # Vertices input
  for _ in range(0, V):
    i = input().split(' ')
    vIndex = int(i[0])
    del i[0:2]
    neighbors = list(map(int, i))
    neighbors.sort()
    g[vIndex] = { 'd': None, 'l': None, 'neighbors': neighbors}

  stack = []
  visited = []
  
  # Visitations
  for rootVertex in range(0, V):
  
    if (rootVertex not in visited):
      
      stack.append(rootVertex)

      step = -1

      while(len(stack) != 0):

        step += 1

        vID = stack.pop()
        while vID in stack: stack.remove(vID)
        visited.append(vID)
      
        v = g[vID]

        v['d'] = step
        v['l'] = step

        # Verify Lowest
        visitedNeighbors = []
        for i in range(0, len(v['neighbors'])):
          if v['neighbors'][i] in visited: visitedNeighbors.append(v['neighbors'][i])
        if (len(visitedNeighbors) > 1):
          lowest = v['l']
          for i in range(0, len(visitedNeighbors)):
            if (g[visitedNeighbors[i]]['l'] < lowest): lowest = g[visitedNeighbors[i]]['l']
          v['l'] = lowest
          currentV = visited[len(visited)-1]
          for i in range(len(visited)-2, -1, -1):
            if visited[i] in g[currentV]['neighbors']:
              if (g[visited[i]]['l'] == lowest): break
              g[visited[i]]['l'] = lowest
              currentV = visited[i]
        
        for i in range(0, len(v['neighbors'])):
          nID = v['neighbors'][i]
          if nID not in visited: stack.append(nID)

  # Critical Links
  criticalLinks = []
  for vID in range(0, V):
    v = g[vID]
    for j in range(0, len(v['neighbors'])):
      nID = v['neighbors'][j]
      n = g[nID]
      if (v['d'] < n['l']): 
        if (vID < nID): criticalLink = str(vID) + ' - ' + str(nID) 
        else: criticalLink = str(nID) + ' - ' + str(vID)
        criticalLinks.append(criticalLink)

  print(str(len(criticalLinks)) + ' critical links')
  for cl in range(0, len(criticalLinks)): print(criticalLinks[cl])
  print('')
  try:
    input()
  except EOFError:
    break
