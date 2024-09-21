# Kann ich dir etwas ausgeben? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/for-loops/002/)
def print_elements(to_print: list) -> None:
  for element in to_print:
    print(element)

if __name__ == '__main__':
  print_elements(['C', 'Y', 'B', 'E', 'R'])
  print_elements(list("CyBeR"))
  print_elements(list(range(0,10)))
  print_elements(list(range(0, -10, -1)))
  print_elements(list(range(-1, -11, -1)))
  print_elements(list(range(0, len("test string") + 1)))
  # noinspection PyTypeChecker
  print_elements(reversed(list("CyBeR")))