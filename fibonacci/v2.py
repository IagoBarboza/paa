memo = [None]*6
counter = 0

def fib(n):
  global counter 
  counter += 1
  if(memo[n]): return memo[n]
  if(n <= 2): f = 1 # This is the considerated operation for the time complexity calculation
  else: f = fib(n-1) + fib(n-2)
  memo[n] = f
  print(memo)
  return f

print(fib(5))
print(counter)