values = [1,5,8,9,10]
memo = [None]*6 # [None, dp(1), dp(2), dp(3), dp(4), dp(5)]

def dp(n):

  if (memo[n]): return memo[n]
  else: 
    if (n == 0): return 0
    else:
      best = 0
      for i in range(0, n): best = max(best, values[i] + dp(n-i-1))
      memo[n] = best
      return best


print(dp(5))