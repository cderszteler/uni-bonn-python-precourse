# Ich kann mir schon eine Schleife binden! (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/for-loops/004/)
if __name__ == '__main__':
  for index in range(5):
    print(index)

  example = ["Hallo", "ich", "bin", "im", " Programm ", " gefangen "]
  for index in range(len(example)):
    print(example[index])

  initial = 1
  while initial <= 2048:
    initial *= 2

  command = ''
  while command != 'exit':
    command = input('Geben Sie einen Befehl ein: ')

  command = 0
  while int(command) < 10:
    number = input('Geben Sie eine Zahl ein: ')
    if number.isdigit():
      command = int(number)

  a = 0
  b = 1
  while a > 10 and b > 40:
    a += 2
    b *= 6