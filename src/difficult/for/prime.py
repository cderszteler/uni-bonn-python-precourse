# Mit alten Griechen sieben (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-500/for-loops/002/)
import math

if __name__ == '__main__':
  inputValue = input('Gib eine Grenze ein: ')
  if not inputValue.isdigit():
    print('Bitte gib eine natürliche Zahl ein!')
    exit()
  limit = int(inputValue)

  marked = [False for repeat in range(limit - 1)]

  for index in range(2, math.ceil(math.sqrt(limit))):
    if not marked[index - 2]:
      print(index)
      for noPrime in range(index * index, limit + 1, index):
        marked[noPrime - 2] = True

  for rest in range(math.ceil(math.sqrt(limit)), limit + 1):
    if not marked[rest - 2]:
      print(rest)
