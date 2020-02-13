i = list(map(int, input().split(' ')))
V = i[0] 
E = i[1]

d = []

for v in range(0, V): 
  d.append([float('inf')]*V)
  d[v][v] = 0

for _ in range(0, E):
  i = list(map(int, input().split(' ')))
  vL = i[0]
  vC = i[1]
  distance = i[2]
  d[vL][vC] = d[vC][vL] = distance

for k in range(0, V):

  od = []

  for v in range(0, V): 
    od.append([None]*V)
    od[v][v] = 0

  # Repeat de k-line and k-column
  od[k] = d[k]
  for l in range(0, V): od[l][k] = d[l][k]

  for vL in range(0, V):
    for vC in range(0, V):
      od[vL][vC] = od[vC][vL] = min(d[vL][vC], d[vL][k] + d[k][vC])

  d = od

longest = [0]*V

for hV in range(0, V):
  for vV in range(0, V):
    if (d[hV][vV] > longest[hV]): longest[hV] = d[hV][vV]

print(min(longest))
