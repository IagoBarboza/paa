a = []
maxSum = 0

n = input()

for i in range(n):
  a.append(int(input()))

for first in range(n):
  for last in range(first, n):
    sum = 0
    for current in range(first, last):
      sum += a[current]
    
    if(sum > maxSum): maxSum = sum

print(maxSum)
      
      
