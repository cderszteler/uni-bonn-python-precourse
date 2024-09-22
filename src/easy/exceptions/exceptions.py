# Keine Macht den Ausnahmen (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/exceptions/001/)
if __name__ == '__main__':
  # print(5/0)
  try:
    int('ich bin coooul')
  except ValueError:
    print("invalid type conversion: 'ich bin coooul' is not a number")

  # pokemon = ["glumanda", "shiggy", "bisasam"]
  # if pokemon[3] == "pikachu": # 3 is out of bounds
  #     print("Bester Starter!")

  empty = {}
  try:
    no_value = empty[0]
  except KeyError:
    print("missing key: '0' is not a key in dictionary 'empty' ")
