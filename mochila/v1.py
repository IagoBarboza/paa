p = [100, 70, 50, 10]
w = [10, 4, 6, 12]

def dp(i, rc):
  
  if(i == len(p) or rc == 0): return 0

  if(w[i] > rc): return dp(i+1, rc)

  return max(p[i] + dp(i+1, rc - w[i]), dp(i+1, rc))

print(dp(0,12))