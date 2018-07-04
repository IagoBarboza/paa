accumulator = input()

while (True):
  try: 
    lastNumber = raw_input()
    if (lastNumber != ''): 
      accumulator = int(accumulator) * int(lastNumber)      
    else: break
      
  except EOFError:
    break

print("Prod = " + str(accumulator))