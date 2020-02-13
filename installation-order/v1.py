import heapq

def bfs(graph, dependencyCounters):

  queue = []
  answer = ''
  
  for i in range(1, len(dependencyCounters)+1):
    if (dependencyCounters[i] == 0): heapq.heappush(queue, i)

  while (len(queue) > 0):

    v = heapq.heappop(queue)
    answer = answer + ' ' + str(v)

    vDependents = graph[v]

    for i in range(0, len(vDependents)):
      dependent = vDependents[i]
      dependencyCounters[dependent] -= 1
      if (dependencyCounters[dependent] == 0): heapq.heappush(queue, dependent)
  
  answer = answer.replace(' ', '', 1)

  if (len(answer.split(' ')) != len(graph)): return 'Impossible'

  return answer 

# graph = {1: [], 2: [1, 6], 3: [1], 4: [3], 5: [3], 6: []}
# dependencyCounters = {1: 2, 2: 0, 3: 2, 4: 0, 5: 0, 6: 1}
# print(bfs(graph, dependencyCounters))

i = list(map(int, input().split(" ")))
numberOfPrograms = i[0]
numberOfDependencies = i[1]

graph = {}
dependencyCounters = {}

for i in range(1, numberOfPrograms+1):
  graph[i] = []
  dependencyCounters[i] = 0

for i in range(0, numberOfDependencies):
  i = list(map(int, input().split(" ")))
  vDependent = i[0]
  v = i[1]
  graph[v].append(vDependent)
  dependencyCounters[vDependent] += 1

print(bfs(graph, dependencyCounters))