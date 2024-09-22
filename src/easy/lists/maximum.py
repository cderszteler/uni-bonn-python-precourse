# Wer ist der Größte? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/listen/002/)
if __name__ == '__main__':
  to_compute: list[int] = [4, 3, 8, 2]
  list_max = None
  for number in to_compute:
    if list_max is None or number > list_max:
      list_max = number
  print(f'Largest number: {list_max}')