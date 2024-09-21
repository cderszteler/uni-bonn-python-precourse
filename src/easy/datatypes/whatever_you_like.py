# Ich bin, was auch immer du willst (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/datentypen/001/)
if __name__ == '__main__':
  # 1.
  print(bool([]))
  print(bool([1, 2, 3]))
  print(bool([1]))
  print(bool(""))
  print(bool("python"))

  # 2.
  print(bool(1))
  print(bool(0))
  print(bool(1.0))
  print(bool(0.0))
  print(bool(0.5))

  # 3.
  print(float(42))
  print(int(42.42))

  # 4.
  print(str(1))
  print(list("python"))
  print(str(True))

  # 5.
  print(int(True))
  print(float(True))

  # 6.
  print(int('Python'))
  # Following do not work:
  # print(list(69))
  # print(list(True))