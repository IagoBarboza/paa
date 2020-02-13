def mergeSort(left, right):

  global a
  global counter

  if(left < right):
    
    mid = int((left + right)/2)

    mergeSort(left, mid)
    mergeSort(mid+1, right)

    sorted = []
    
    leftIndex = left
    rightIndex = mid+1

    leftLimit = mid+1
    rightLimit = right+1

    while(True):

      if(leftIndex == leftLimit and rightIndex == rightLimit): break

      if(leftIndex == leftLimit):
        sorted.append(a[rightIndex])
        rightIndex += 1

      elif(rightIndex == rightLimit):
        sorted.append(a[leftIndex])
        leftIndex += 1

      elif(a[leftIndex] == a[rightIndex]):
        sorted.append(a[leftIndex])
        leftIndex += 1

      elif(a[leftIndex] < a[rightIndex]):
        sorted.append(a[leftIndex])
        leftIndex += 1
      
      elif(a[leftIndex] > a[rightIndex]):
        counter += (mid - leftIndex + 1)
        sorted.append(a[rightIndex])
        rightIndex += 1
      
    for i in range(0, len(sorted)):
      a[i+left] = sorted[i]

cases = int(input())

for c in range(cases):

  counter = 0
  
  input()

  aSize = int(input())

  a = []

  while(len(a) < aSize):
    a.append(int(input()))

  mergeSort(0, len(a)-1)

  print(counter)