# Nah an Pi ran! (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/logik/003/)
def approximate_pi(precision: int) -> float:
  approximation = 0
  for index in range(precision):
    approximation += (1 / (2 * index + 1)) * ((-1)**index)
  return 4 * approximation


if __name__ == '__main__':
  n = input("Genauigkeit: ")
  if n == '-1':
    print(3)
    exit()
  elif not n.isdigit():
    print("Bitte gib eine ganze Zahl ein!")
    exit()
  pi = approximate_pi(int(n))
  print(pi)