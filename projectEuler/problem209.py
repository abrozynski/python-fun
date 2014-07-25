import math

# The input array can be any length, as long as it contains only zeros and ones




def andTable(inputs):
  if type(inputs) == str:
    input_array = []
    for i in range(0, len(inputs)):
      input_array.append(int(inputs[i]))
    return andTable(input_array)  

  print inputs
  if sum(inputs) == len(inputs):
    return '1'
  else:
    return '0'

def xORTable(inputs):
  if type(inputs) == str:
    input_array = []
    for i in range(0, len(inputs)):
      input_array.append(int(inputs[i]))
    return andTable(input_array)  
  if sum(inputs) == 1:
    return 1
  else:
    return 0


def generateInputs(length):
  inputs =[]
  for i in range(2**length):
    x = bin(i)[2:]
    while len(x) < length:
      x = addZeros(x)
    inputs.append(x)
  return inputs
    

def addZeros(number):
  return '0'+number


def problem209():
  inputs=generateInputs(6)
  counter = 0
  for x in inputs:
    if andTable(x[1]+x[2]+x[3]+x[4]+x[5]+ xORTable(x[0]+ andTable(x[1]+x[2]))) == '0':
      counter += 1
  return counter
