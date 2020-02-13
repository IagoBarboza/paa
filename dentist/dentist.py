def mergeSort(left, right):

  global a

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

      elif(a[leftIndex][1] == a[rightIndex][1]):
        sorted.append(a[leftIndex])
        leftIndex += 1

      elif(a[leftIndex][1] < a[rightIndex][1]):
        sorted.append(a[leftIndex])
        leftIndex += 1
      
      elif(a[leftIndex][1] > a[rightIndex][1]):
        sorted.append(a[rightIndex])
        rightIndex += 1
      
    for i in range(0, len(sorted)):
      a[i+left] = sorted[i]

a = []

n = input()

for i in range(0, n):
  c = raw_input().split(" ")
  a.append([int(c[0]), int(c[1])])

mergeSort(0, len(a)-1)

selected = [a[0]]

for i in range(1, len(a)):
  if(a[i][0] >= selected[len(selected)-1][1]): selected.append(a[i])

print(len(selected))