# Catch the python (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/for-loops/003/)
if __name__ == '__main__':
  dct = {'Hallo ': 'Welt ', 'Antwort ': 42, 'Python ': 'cool!'}
  for key, value in dct.items():
    print('Key: ', key)
    print('Value: ', value)
