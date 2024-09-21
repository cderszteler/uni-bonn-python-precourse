# Wer kommt öfters (vor)? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/for-loops/005/)
from collections import Counter

names = [
  "marcell d'avis", 'mar', 'marc', "marcell d'avis", "marcell d'avis",
  'mar', "marcell d'avis", "marcell d'avis", 'avis', "marcell d'avis",
  "marcell d'avis", 'avis', "marcell d'avis", 'avis', 'marc', 'avis',
  'marc', 'marc', 'avis', 'marc', 'avis', "marcell d'avis",
  "marcell d'avis", "marcell d'avis", "marcell d'avis", 'avis', 'avis',
  "marcell d'avis", 'mar', "marcell d'avis", "marcell d'avis", 'avis',
  'mar', 'mar', 'marc', 'mar', 'mar', 'avis', 'avis', "marcell d'avis",
  "marcell d'avis", 'mar', "marcell d'avis", 'marc', 'marc',
  "marcell d'avis", 'mar', "marcell d'avis", 'mar', 'mar', 'marc',
  "marcell d'avis", 'mar', 'mar', 'mar', "marcell d'avis", 'marc',
  'marc', "marcell d'avis", "marcell d'avis", "marcell d'avis",
  "marcell d'avis", 'avis', 'mar', "marcell d'avis", "marcell d'avis",
  'mar', 'avis', 'avis', 'mar', 'marc', "marcell d'avis", 'avis',
  "marcell d'avis", 'marc', 'marc', 'avis', 'mar', 'mar', 'marc', 'avis',
  'mar', "marcell d'avis", "marcell d'avis", 'mar', "marcell d'avis",
  "marcell d'avis", 'marc', "marcell d'avis", 'avis', 'mar',
  "marcell d'avis", "marcell d'avis", 'mar', 'marc', 'avis', 'avis',
  "marcell d'avis", "marcell d'avis", 'avis', "marcell d'avis", 'avis',
  'marc', 'marc', 'mar', 'marc', "marcell d'avis", 'mar', 'mar',
  "marcell d'avis", 'mar', "marcell d'avis", "marcell d'avis", 'marc',
  "marcell d'avis", 'marc', 'marc', 'marc', "marcell d'avis",
  "marcell d'avis", 'marc', 'marc', "marcell d'avis", "marcell d'avis",
  "marcell d'avis", "marcell d'avis", 'marc', "marcell d'avis", 'marc',
  'mar', 'marc', 'marc', 'avis', 'marc', "marcell d'avis", 'mar', 'marc',
  'mar', 'mar', 'marc', 'avis', 'marc', "marcell d'avis", 'mar',
  "marcell d'avis", "marcell d'avis", 'avis', 'mar', "marcell d'avis",
  'avis', 'mar', 'marc', 'mar', "marcell d'avis", 'mar', 'mar', 'marc',
  'mar', "marcell d'avis", 'mar', 'marc', 'marc', "marcell d'avis",
  'marc', "marcell d'avis", 'avis', 'marc', 'avis', "marcell d'avis",
  "marcell d'avis", "marcell d'avis", "marcell d'avis", 'avis', 'marc',
  'avis', 'marc', 'mar', "marcell d'avis", "marcell d'avis",
  "marcell d'avis", "marcell d'avis"
]

if __name__ == '__main__':
  counter = Counter(names)
  print(f'"Marcell d\'avis" in der Liste: {counter["marcell d'avis"]}')
  print(f'"Marc" in der Liste: {counter["marc"]}')
  print(f'Es sind {len(Counter(set(names)))} einzigartige Einträge in der Liste.')
  print(f'Es gibt {len(list(filter(lambda name: name.startswith('marc'), names)))} Einträge, die mit "marc" beginnen.')
