# Ausnahmsweise (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/exceptions/001/)
def divide():
  try:
    zahl1 = float(input('Gib die erste Zahl ein: '))
    zahl2 = float(input('Gib die zweite Zahl ein: '))
    return zahl1 / zahl2
  except ValueError:
    print('Das ist keine Zahl!')
  except ZeroDivisionError:
    print('Du darfst nicht durch Null teilen!')
  print('Die Funktion ist beendet .')

if __name__ == '__main__':
  print(divide())