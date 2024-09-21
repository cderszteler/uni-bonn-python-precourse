# Der Aufstieg der Flowcharts (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/flowcharts/003/)
if __name__ == '__main__':
  n = input('Gib eine ganze Zahl ein: ')
  if not n.isdigit():
    print('Bitte gib eine ganze Zahl ein (n>0).')
    exit()
  n = int(n)
  faculty = 1
  while n > 1:
    faculty *= n
    n = n - 1
  print(f'Fakultät: {faculty}')