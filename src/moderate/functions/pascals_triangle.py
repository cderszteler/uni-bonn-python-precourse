# Pascalsches Dreieck (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/funktionen/002/)

# See https://stackoverflow.com/questions/15580291/how-to-efficiently-calculate-a-row-in-pascals-triangle
def calculate_line(order: int) -> list[int]:
  line = [1]
  for value in range(order):
    line.append(int(line[value] * (order - value) / (value + 1)))
  return line

def calculate_pascals_triangle(max_order: int) -> list[list[int]]:
  triangle = [[1]]
  for order in range(2, max_order + 1):
    triangle.append(calculate_line(order))
  return triangle

if __name__ == '__main__':
  print(calculate_line(3))
  print(calculate_pascals_triangle(5))