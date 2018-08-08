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
          sumA = a[first]
          if (sumA > maxSum):
            maxSum = sumA
            begin = end = first
        else:
          sumB = 0
          for k in range(first, last+1):
            sumB = sumB + a[k]
            if (sumB > maxSum):
              maxSum = sumB
              begin = first
              end = last
    print "maxSum: " + str(maxSum)
    print "begin: " + str(begin)
    print "end: " + str(end)
  else: 
    break
  