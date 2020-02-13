def fib(n):
  f = [None]*(n+1)
  f[1] = 1
  f[2] = 1
  for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]
  print(f)
  return f[n]

print(fib(6))
