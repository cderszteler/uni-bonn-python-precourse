# (Un)ordentliche Listen (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/listen/005/)
def first_task() -> list[int]:
  given = [1, 2, 3, 4, 5, 6, 7]
  given.reverse()
  return given

def second_task() -> list[int]:
  given = [1, 2, 3, 4, 5, 6, 7]
  del given[3]
  return given

def third_task() -> list[int]:
  given = [1, 2, 3, 4, 5, 6, 7]
  return given[2:5]

def fourth_task() -> list[int]:
  given = [1, 2, 3, 4, 5, 6, 7]
  del given[2]
  given.insert(1, 3)
  return given

def fifth_task() -> list[int]:
  # noinspection PyListCreation
  given = [1, 2, 3, 4, 5, 6, 7]
  given.append(8)
  return given

def sixth_task() -> list[int]:
  given = [1, 2, 3, 4, 5, 6, 7]
  given.insert(0, 0)
  return given

def seventh_task() -> list[int]:
  given = [1, 2, 3, 4, 5, 6, 7]
  return given[1:3] + given[-2:]

def eighth_task() -> list[int]:
  given = [1, 2, 3, 4, 5, 6, 7]
  del given[:2]
  del given[1]
  del given[-1]
  given.append(1)
  given.insert(1, 7)
  return given

if __name__ == '__main__':
  print(first_task())
  print(second_task())
  print(third_task())
  print(fourth_task())
  print(fifth_task())
  print(sixth_task())
  print(seventh_task())
  print(eighth_task())