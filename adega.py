def dp(b,e,y):
    
    if (b == e): 
        return prices[b]*y
    else: 
        key = str(b)+'_'+str(e)            
        try:
            best = memo[key]
        except KeyError:        
            best = max(prices[b]*y+dp(b+1,e,y+1), prices[e]*y+dp(b,e-1,y+1))
            memo[key] = best
        return best

while (True):
    try: 
        n = input()
        n = int(n)
        if (n>0):
            prices = []
            memo = {}
            for i in range(n):
                insertedPrice = input()
                insertedPrice = int(insertedPrice)
                prices.append(int(insertedPrice))
            print(dp(0,len(prices)-1,1))
        else:
            print(0)
        
    except EOFError:
        break