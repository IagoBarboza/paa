memo = {}
def dp(n,k,d):
  try:
    if (memo[str(n)+'-'+str(d)] != None): return memo[str(n)+'-'+str(d)]
  except:
    counter = 0
    for i in range (1, k+1):
      if (i < n):
        if(i >= d): counter += dp(n-i, k, 0)
        else: counter += dp(n-i, k, d)
      elif (i == n): 
        if (i >= d): counter += 1
        break
    memo[str(n)+'-'+str(d)] = counter
    return counter

i = list(map(int, input().split(" ")))
r = dp(i[0], i[1], i[2])
print(r % ((10 ** 9) + 7))
