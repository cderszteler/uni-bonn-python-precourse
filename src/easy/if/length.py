# Alles eine Frage der Länge? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/if-abfragen/003/)
if __name__ == '__main__':
  to_check = []
  if len(to_check) > 20:
    print('Riesig')
  elif len(to_check) > 10:
    print('Groß')
  else:
    print('Klein')