# Total tolle Tasks mit total tollen Strings (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/strings/002/)
if __name__ == '__main__':
  great_string = " total tolle Tage hier im Vorkurs "
  print(great_string.strip())
  print("Wir haben" + great_string + "!")
  print(great_string.replace('Vorkurs', 'total tollen Vorkurs'))
  print(great_string.replace('total', 'super'))
  print(great_string.replace('t', 'T'))
  print(great_string.upper())
  print(great_string[::-1])
  print(great_string[::2])
  print(great_string.strip().split(' ')[::2])
  print(list(filter(lambda words: words.lower().startswith('t'), great_string.split(' '))))