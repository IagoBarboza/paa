def dp(n): 
    
    memo = []
    memo.append(0)
    for m in range(1, n+1):
        memo.append(-1)

    for j in range(1, n+1):
        best = 0

        for i in range(j):
            best = max(best, v[i] + memo[j-i-1])
        
        memo[j] = best
    
    return memo[n]

while(True):
    n = input()
    if (n == 0):
        break
    else:
        v = []
        for i in range(n):
            v.append(int(input()))
        
        memo = []
        for i in range(n+1):
            memo.append(-1)
        
        print(dp(n))
