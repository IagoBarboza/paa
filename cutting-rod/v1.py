values = [1,5,8,9,10]

def dp(n):
  if (n == 0): return 0
  else:
    best = 0
    for i in range(0, n): best = max(best, values[i] + dp(n-i-1))
    return best

print(dp(5))