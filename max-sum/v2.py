a = []
maxSum = 0

n = input()

for i in range(n):
  a.append(int(input()))

for first in range(n):
  sum = 0
  for last in range(first, n):
    sum += a[last]

  if(sum > maxSum): maxSum = sum

print(maxSum)
      
      
