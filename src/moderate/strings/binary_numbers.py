# Einfach zählen! (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/strings/005/)
def convert(number: int, reverse=False) -> str:
  binary = bin(number)[2:]
  return binary if not reverse else binary[::-1]

def main():
  print(convert(1))
  print(convert(2))
  print(convert(10))
  print(convert(10, reverse=True))

if __name__ == '__main__':
  main()