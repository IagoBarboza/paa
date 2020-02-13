class Node:
  even = 0
  odd = 0
  left = None
  right = None
  leftChild = None
  rightChild = None
  parent = None

def build(parent, left, right):

  node = Node()
  node.parent = parent
  node.left = left
  node.right = right

  if(left == right): 
    if(a[left] % 2 == 0): node.even += 1
    else: node.odd += 1
    return node

  mid = int((left + right)/2)

  leftChild = build(node, left, mid)
  rightChild = build(node, mid+1, right)
  
  node.leftChild = leftChild
  node.rightChild = rightChild
  node.even = leftChild.even + rightChild.even
  node.odd = leftChild.odd + rightChild.odd

  return node

def queryEven(node, left, right):
  
  if(right < node.left or left > node.right): 
    return 0

  if(node.left >= left and node.right <= right): 
    return node.even

  else:
    return queryEven(node.leftChild, left, right) + queryEven(node.rightChild, left, right)

def queryOdd(node, left, right):
  
  if(right < node.left or left > node.right): 
    return 0

  if(node.left >= left and node.right <= right): 
    return node.odd

  else:
    return queryOdd(node.leftChild, left, right) + queryOdd(node.rightChild, left, right)

def search(node, i):
  if(node.left == node.right):
    if(node.left == i): return node

  else:
    mid = int((node.left + node.right)/2)
    if (i <= mid): return search(node.leftChild, i)
    else: return search(node.rightChild, i)

def update(node, value):
  
  if(value % 2 == 0):
    node.even += 1
    node.odd -= 1
  
  else: 
    node.even -= 1
    node.odd += 1
  
  if(node.parent): update(node.parent, value)

input()

a = list(map(int, input().split()))
a.insert(0,-1)

root = build(None, 1, len(a)-1)

numberOfOperations = int(input())

for i in range(0, numberOfOperations):
  
  params = list(map(int, input().split(" ")))
  
  if(params[0] == 0):
    node = search(root, params[1])
    if((a[node.left] % 2 == 0 and params[2] % 2 != 0) or (a[node.left] % 2 != 0 and params[2] % 2 == 0)): 
      a[node.left] = params[2]
      update(node, params[2])
  elif(params[0] == 1): print(queryEven(root, params[1], params[2]))
  elif(params[0] == 2): print(queryOdd(root, params[1], params[2]))

