# Kundenzufriedenheit (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/strings/001/)
if __name__ == '__main__':
  example = "marcell "
  example += "d'avis"

  print(example[2])
  print(example[:4])
  print(example[8:])
  print(example[3] + example[-1])

  print(example.upper())
  print(example.index('c'))
  print(example.startswith('cyber'))
  print(example.islower())
  print(example.split(' '))
  print(example.replace('l', 'm'))