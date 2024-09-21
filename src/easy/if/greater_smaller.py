# Größer und kleiner (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/if-abfragen/001/)
if __name__ == '__main__':
  n = int(input('Gib eine Zahl ein: '))
  if 5 <= n <= 10:
    print(f'{n} ist zwischen 5 und 10')
  else:
    print(f'{n} ist nicht zwischen 5 und 10')