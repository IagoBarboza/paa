import sys

sys.setrecursionlimit(2**30)

def dp(pid, cf):

  if(pid > NOP): return 0
  
  if (pid, cf) in memo: return memo[(pid,cf)]
  
  program = programs[pid]

  minEDP = float("inf")

  for f in range(0, NOF):
    
    edp = program[f]
    
    if (f == cf):
      minEDP = min(minEDP, edp + dp(pid+1, cf))
    
    else: 
      minEDP = min(minEDP, edp + CFC + dp(pid+1, f))
  
  memo[(pid,cf)] = minEDP
  return minEDP

NOF = 1
NOP = 1
CFC = 1

while(NOF * NOP * CFC != 0):
  
  memo = {}

  i = list(map(int, input().split(" ")))
  NOF = i[0]
  NOP = i[1]
  CFC = i[2] * i[3]

  if (NOF * NOP * CFC != 0):

    programs = {}

    for p in range(1, NOP+1):
      programs[p] = []
      for f in range(0, NOF):
        i = list(map(int, input().split(" ")))
        programs[p].append(i[0]*i[1])

    print(dp(1,0))