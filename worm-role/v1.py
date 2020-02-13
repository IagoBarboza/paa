c = int(input())

while(c > 0):
  c -= 1

  g = []

  i = list(map(int, input().split(" ")))
  V = i[0]
  E = i[1]

  d = [float("inf")]*V
  d[0] = 0

  for e in range(0, E):
    i = list(map(int, input().split(" ")))
    g.append({'from': i[0], 'to': i[1], 'w': i[2]})

  for i in range(0, V-1):
    for e in range(0, E):
      if (d[g[e]['from']] + g[e]['w'] < d[g[e]['to']]): d[g[e]['to']] = d[g[e]['from']] + g[e]['w']

  dBackup = d.copy()

  for e in range(0, E):
    if (d[g[e]['from']] + g[e]['w'] < d[g[e]['to']]): d[g[e]['to']] = d[g[e]['from']] + g[e]['w']

  possible = False

  for i in range(0, V):
    if (d[i] < dBackup[i]): 
      possible = True
      break
  
  if (possible): print('possible')
  else: print('not possible')
