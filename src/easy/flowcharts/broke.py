# Flowcharts: A Python story (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/flowcharts/004/)
if __name__ == '__main__':
  n = input('')
  if n.startswith('Bin broke, weil Schischa'):
    print('Wyld')
  elif n.startswith('Bin broke') and len(n) != 9:
    print('Digga')
  elif len(n) == 9:
    print('Auf Lock')
  else:
    print('Zwambo')