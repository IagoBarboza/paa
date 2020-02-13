def searchLo(x, left, right):
  if(left == right):
    if(a[left] >= x): return left
    else: return None

  mid = int((left+right)/2)

  if(a[mid] >= x): 
    if(mid == left): return mid
    if(mid > left):
      mostLeft = searchLo(x, left, mid-1)
      if(mostLeft == None): return mid
      else: return mostLeft 
  else: return searchLo(x, mid+1, right)

def searchHi(x, left, right):
  if(left == right):
    if(a[left] <= x): return left
    else: return None

  mid = int((left+right)/2)

  if(a[mid] <= x):
    mostRight = searchHi(x, mid+1, right)
    if(mostRight == None): return mid
    else: return mostRight
  else: 
    if(mid != left): return searchHi(x, left, mid-1)

input()

a = list(map(int, input().split(" ")))

nQueries = int(input())

queriesArray = []

for q in range(nQueries):
  queriesArray.append(int(input()))

for q in range(nQueries):
  x = queriesArray[q]
  print(searchLo(x, 0, len(a)-1), searchHi(x, 0, len(a)-1))
