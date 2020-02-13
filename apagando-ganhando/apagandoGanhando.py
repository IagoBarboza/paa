def ndInput():
  global n
  global d
  n, d = list(map(int, input().split(" ")))

ndInput()

while(n != 0 and d != 0):

  a = [int(c) for c in input()]

  sArraySize = n - d
  
  sArray = [a[0]]

  for i in range(1, n):

    if(a[i] <= sArray[len(sArray)-1]):
      if(len(sArray) < sArraySize):
        sArray.append(a[i])

    else:
      while(len(sArray) and len(sArray)-1 + (n-i) >= sArraySize and a[i] > sArray[-1]):
        sArray.pop(-1)
      sArray.append(a[i])
      
  print(''.join(list(map(str,sArray))))

  ndInput()

  