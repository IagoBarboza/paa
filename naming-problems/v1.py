# g = [
#   { #0
#     'letter': None,
#     'problem': False,
#     'name': None,
#     'neighbors': { 1:1, 2:1},
#     'pi': None,
#   },
#   { #1
#     'letter': None,
#     'problem': True,
#     'name': None,
#     'neighbors': { 0:0, 6:1, 7:1 },
#     'pi': None,
#   },
#   { #2
#     'letter': None,
#     'problem': True,
#     'name': None,
#     'neighbors': { 0:0, 8:1 },
#     'pi': None,
#   },
#   { #3
#     'letter': 'A',
#     'problem': False,
#     'name': None,
#     'neighbors': { 5:1, 6:0, 8:0 },
#     'pi': None,
#   },
#   { #4
#     'letter': 'B',
#     'problem': False,
#     'name': None,
#     'neighbors': { 5:1, 7:0 },
#     'pi': None,
#   },
#   { #5
#     'letter': None,
#     'problem': False,
#     'name': None,
#     'neighbors': { 3:0, 4:0 },
#     'pi': None,
#   },
#   { #6
#     'letter': None,
#     'problem': False,
#     'name': 'apple',
#     'neighbors': { 1:0, 3:1 },
#     'pi': None,
#   },
#   { #7
#     'letter': None,
#     'problem': False,
#     'name': 'banana',
#     'neighbors': { 1:0, 4:1 },
#     'pi': None,
#   },
#   { #8
#     'letter': None,
#     'problem': False,
#     'name': 'ajuda',
#     'neighbors': { 2:0, 3:1 },
#     'pi': None,
#   },
# ]

ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

queue = None
visited = None

def bfs():

  global queue
  global visited

  queue = []
  visited = []
  
  queue.append(0)

  while(len(queue) > 0):

    vi = queue.pop(0)

    visited.append(vi)

    v = g[vi]

    for ni, nec in v['neighbors'].items():
      if nec and ni not in visited and ni not in queue:
        queue.append(ni)
        g[ni]['pi'] = vi

cases = int(input())
for c in range(1, cases+1):
  
  numberOfProblems = int(input())

  # Create the graph with the in-vertice and the out-vertice
  g = [
    {
      'letter': None,
      'problem': False,
      'name': None,
      'neighbors': {},
      'pi': None,
    },
    {
      'letter': None,
      'problem': False,
      'name': None,
      'neighbors': {},
      'pi': None,
    }
  ]

  # Add the problem-vertices in the graph
  for pi in range(2, numberOfProblems+2):
    g[0]['neighbors'][pi] = 1
    g.append({
      'letter': None,
      'problem': True,
      'name': None,
      'neighbors': { 0:0 },
      'pi': None
    })

  # Add the letter-vertices in the graph
  for i in range(0, len(ALPHABET)):
    g.append({
      'letter': ALPHABET[i],
      'problem': False,
      'name': None,
      'neighbors': {1:1},
      'pi': None
    })
    g[1]['neighbors'][len(g)-1] = 0
  
  # Add the names-vertices in the graph
  for pvi in range(2, numberOfProblems+2):
    
    namesArray = input().split(' ')
    namesArray.pop(0)
    
    for n in range(0, len(namesArray)):
   
      name = namesArray[n].capitalize()
      lvi = numberOfProblems + 2 + ALPHABET.index(name[0])

      g.append({
        'letter': None,
        'problem': False,
        'name': name,
        'neighbors': {lvi:1, pvi:0},
        'pi': None
      })

      g[lvi]['neighbors'][len(g)-1] = 0
      g[pvi]['neighbors'][len(g)-1] = 1

  bfs()

  while(g[1]['pi'] != None):

    # Mount the path array
    v = g[1]
    path = [1]
    while (v['pi'] != None):
      path.insert(0, v['pi'])
      v = g[v['pi']]

    # Apply the edge usage in the path
    for i in range(0, len(path)-1):
      g[path[i]]['neighbors'][path[i+1]] = 0
      g[path[i+1]]['neighbors'][path[i]] = 1

    # Remove all the parent index
    for i in range(0, len(g)):
      g[i]['pi'] = None

    bfs()

  names = []

  for i in range(0, len(g)):
    if g[i]['problem']:
      for ni, nec in g[i]['neighbors'].items():
        if g[ni]['name'] and not nec: names.append(g[ni]['name'].capitalize())

  names.sort()
  print('Case #'+str(c)+':')
  for n in range(0, len(names)):
    print(names[n])