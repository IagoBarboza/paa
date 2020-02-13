class Node:
  value = None
  left = None
  right = None
  leftChild = None
  rightChild = None
  parent = None

a = [-1,5,2,8,9,3,6]


def build(parent=None, left=1, right=len(a)):

  global a

  node = Node()
  node.parent = parent
  node.left = left
  node.right = right

  if(right - left < 2): 
    node.value = a[left]
    return node

  mid = int((right + left)/2)

  leftChild = build(node, left, mid)
  rightChild = build(node, mid, right)
  
  node.leftChild = leftChild
  node.rightChild = rightChild
  node.value = leftChild.value + rightChild.value

  return node

def query(node, left, right):
  
  if(right <= node.left or left >= node.right): 
    return 0

  if(node.left >= left and node.right <= right): 
    return node.value

  else:
    return query(node.leftChild, left, right) + query(node.rightChild, left, right)

def search(node, i):
  
  if(node.right - node.left < 2):
    if(node.left == i): return node

  else:
    mid = int((node.left + node.right)/2)
    if (i < mid): return search(node.leftChild, i)
    else: return search(node.rightChild, i)

def update(node, value):
  nodeOldValue = node.value
  node.value = value
  if(node.parent): update(node.parent, node.parent.value - nodeOldValue + node.value)
  
root = build()
node = search(root, 1)
update(node, 10)