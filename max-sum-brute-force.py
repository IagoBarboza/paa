while (True):
  n = raw_input()
  maxSum = 0
  begin = end = -1
  if (n):
    n = int(n)
    a = []
    for i in range(0, n):
      a.append(input())
    for first in range(0, n):
      for last in range(first, n):
        if (first == last):
          sum = a[first]
          if (sum > maxSum):
            maxSum = sum
            begin = end = first
        else:
          sum = 0
          for k in range(first, last+1):
            sum = sum + a[k]
            if (sum > maxSum):
              maxSum = sum
              begin = first
              end = last
    print "maxSum: " + str(maxSum)
    print "begin: " + str(begin)
    print "end: " + str(end)
  else: 
    break
  