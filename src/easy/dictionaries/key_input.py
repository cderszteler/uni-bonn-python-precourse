# Schlüssel durch input hinzufügen (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/dictionaries/002/)
if __name__ == '__main__':
  my_dict = {}

  key = input('Enter a key: ')
  value = input('Enter a value: ')
  my_dict[key] = value
  print(my_dict)

  if 'cyber' in my_dict.keys() and 'cyber' in my_dict.values():
    print('DOUBLE CYBER!')
  elif 'cyber' in my_dict.keys():
    print('CYBER')
  elif 'cyber' in my_dict.values():
    print('cyber!')