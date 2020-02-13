p = [100, 70, 50, 10]
w = [10, 4, 6, 12]
memo = [[None]*13, [None]*13, [None]*13, [None]*13, [None]*13] 

def dp(i, rc):

  if(memo[i][rc] != None): return memo[i][rc]

  if(i == len(p) or rc == 0): memo[i][rc] = 0

  elif(w[i] > rc): memo[i][rc] = dp(i+1, rc)

  else: memo[i][rc] = max(p[i] + dp(i+1, rc - w[i]), dp(i+1, rc))
  
  return memo[i][rc]

dp(0,12)
