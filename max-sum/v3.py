a = [-2,11,-4,13,-5,-2]

def dq(left, right):

  if(left == right):
    if(a[left] > 0): return a[left]
    else: return a[right]
  
  else: 
    mid = (left + right) / 2
    
    sum = 0
    maxLeft = 0
    for current in range(mid, left-1, -1):
      sum += a[current]
      if(sum > maxLeft): maxLeft = sum
    
    sum = 0
    maxRight = 0
    for current in range(mid+1, right+1):
      sum += a[current]
      if(sum > maxRight): maxRight = sum

    return max(
      maxLeft+maxRight,
      dq(left, mid),
      dq(mid+1, right)
    )


maxSum = dq(0, 5)
print(maxSum)
