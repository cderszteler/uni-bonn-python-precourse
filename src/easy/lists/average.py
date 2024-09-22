# Nur so durchschnittlich (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/listen/003/)
if __name__ == '__main__':
  to_compute: list[float] = [2, 4, 6.5, 2, 8]
  # Obviously this could also be done by iterating over every element of the list
  # and adding to a variable.
  average = sum(to_compute) / len(to_compute)
  print(f'Average: {average}')