# Wahr oder falsch (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/if-abfragen/002/)
if __name__ == '__main__':
  b = bool(input('Gib einen Booleanwert ein: ').lower())
  print('Wahr' if b else 'Falsch')