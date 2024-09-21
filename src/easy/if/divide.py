# Teilen oder nicht teilen? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/if-abfragen/004/)
if __name__ == '__main__':
  n = int(input('Gib mir eine Zahl: '))
  if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
  elif n % 3 == 0:
    print('Fizz')
  elif n % 5 == 0:
    print('Buzz')
  else:
    print(n)