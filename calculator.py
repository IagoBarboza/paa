accumulator = input()
secondNumber = input()
firstOperator = raw_input()

if firstOperator == '+':
  accumulator = float(accumulator) + float(secondNumber)
  print('{0:.3f}'.format(accumulator))  
elif firstOperator == '-': 
  accumulator = float(accumulator) - float(secondNumber)
  print('{0:.3f}'.format(accumulator))  
elif firstOperator == '*':
  accumulator = float(accumulator) * float(secondNumber)
  print('{0:.3f}'.format(accumulator))
elif firstOperator == '/': 
  if (secondNumber != 0):
    accumulator = float(accumulator) / float(secondNumber)      
    print('{0:.3f}'.format(accumulator))
  else: print("operacao nao pode ser realizada")

lastNumber = secondNumber
lastOperator = firstOperator

while (lastOperator != '&'):
  
  lastNumber = input()
  lastOperator = raw_input()
  
  if (lastOperator != '&'):
    if lastOperator == '+':
      accumulator = float(accumulator) + float(lastNumber)
      print('{0:.3f}'.format(accumulator))
    elif lastOperator == '-':
      accumulator = float(accumulator) - float(lastNumber)
      print('{0:.3f}'.format(accumulator))
    elif lastOperator == '*':
      accumulator = float(accumulator) * float(lastNumber)
      print('{0:.3f}'.format(accumulator))
    elif lastOperator == '/': 
      if (lastNumber != 0):
        accumulator = float(accumulator) / float(lastNumber)      
        print('{0:.3f}'.format(accumulator))
      else: print("operacao nao pode ser realizada")


