# Größer und kleiner 2.0 (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/if-abfragen/005/)
if __name__ == '__main__':
  n = input('Gib eine String ein: ')
  if 5 <= len(n) <= 10:
    print(f'{n} hat zwischen 10 und 20 Zeichen')
  else:
    print(f'{n} hat nicht zwischen 10 und 20 Zeichen')