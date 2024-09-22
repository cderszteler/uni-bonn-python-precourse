# Auf die Technik kommt es an (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/listen/006/)
def create_list(dimension: int) -> list[list[int]]:
  wrapper = []
  for index in range(dimension):
    wrapper.append([index + 1] * dimension)
  return wrapper

def first_task(technique: list[list[int]]) -> None:
  print(technique[3])
  print(technique[2][1])
  print([technique[0][0]] + [technique[1][0]] + [technique[3][0]] + [technique[3][0]])

def second_task(technique: list[list[int]]) -> None:
  for index in range(len(technique[0])):
    print(technique[index])
  for index in range(len(technique[0])):
    print([technique[0][index]] + [technique[1][index]] + [technique[2][index]] + [technique[3][index]])

def third_task(technique: list[list[int]]) -> None:
  print(f'Rows: {len(technique[0])}, columns: {len(technique)}')

def fourth_task(technique: list[list[int]]) -> None:
  technique_sum = 0
  for index in range(len(technique[0])):
    row_sum = sum(technique[index])
    technique_sum += row_sum
    print(f'Sum {index}-row: {row_sum}')
  for index in range(len(technique[0])):
    column = [technique[0][index]] + [technique[1][index]] + [technique[2][index]] + [technique[3][index]]
    print(f'Sum {index}-column: {sum(column)}')
  print(f'Sum of list: {technique_sum}')

def fifth_task(technique: list[list[int]]) -> bool:
  for row in range(len(technique)):
    first = technique[row][0]
    for element in range(len(technique[row])):
      if first != technique[row][element]:
        return False
  return True

def sixth_task(technique: list[list[int]]) -> None:
  count = 0
  for row in range(len(technique)):
    count += technique[row].count(1)
  print(f"'1's in list: {count}")

def seventh_task(technique: list[list[int]]) -> None:
  for row in range(len(technique)):
    for element in range(len(technique[row])):
      # We don't want to spam the console
      # print(type(element))
      ""

if __name__ == '__main__':
  technique_list = create_list(4)
  print('Task one:')
  first_task(technique_list)
  print('Task two:')
  second_task(technique_list)
  print('Task three:')
  third_task(technique_list)
  print('Task four:')
  fourth_task(technique_list)
  print('Task fifth:')
  print(fifth_task(technique_list))
  print('Task sixth:')
  sixth_task(technique_list)
  print('Task seventh:')
  seventh_task(technique_list)