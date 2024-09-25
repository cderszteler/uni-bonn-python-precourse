# Money, Money, Money (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/funktionen/001/)

units = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

def calculate_units(amount: float) -> dict[float, int]:
  calculated = {}
  rest = amount
  for unit in units:
    if rest == 0:
      break
    elif unit > rest:
      continue
    amount = rest // unit
    rest = rest % unit
    calculated[unit] = amount
  return calculated


if __name__ == '__main__':
  print(calculate_units(42))
  print(calculate_units(42.99))