def max_sum(left, right):
  
  # stop condition: single element
  if (left == right):
    if (a[left] > 0):
      return a[left]
    else: 
      return 0
  else:
    mid = (left + right) / 2
   
    # max sum in the left side sufix 
    sum = 0
    max_left = 0
    for k in range(mid, left-1, -1):
      sum += a[k]
      if (sum > max_left):
        max_left = sum

    # max sum in the right side prefix
    sum = 0
    max_right = 0
    for k in range(mid+1, right+1):
      sum += a[k]
      if (sum > max_right):
        max_right = sum
  
    # returns the max between the best suffix of the left side plus the best prefix of right side and 
    # the max sum of left side and the max sum of the right side 
    return max(
      max_left + max_right,
      max_sum(left, mid),
      max_sum(mid+1, right)
    )
    
while (True):
  n = raw_input()
  if (n):
    n = int(n)
    a = []
    for i in range(0, n):
      a.append(input())
    print max_sum(0, n-1)
  else: 
    break
  