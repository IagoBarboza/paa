p = [1,5,8,9,10]
memo = [0, None, None, None, None, None]

def dp(n):
  best = 0
  for j in range(0, n+1): # dp(j)
    for i in range (0, j): best = max(best, p[i] + memo[j-i-1])
    memo[j] = best
  return memo[n]

print(dp(5))