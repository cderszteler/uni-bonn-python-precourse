# Sort, sort, sort (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/for-loops/003/)
# #mostInefficientSortAlgorithm
def find_smallest_item(target: list[int]) -> int:
  if len(target) == 0:
    raise ValueError("list is empty")
  smallest = target[0]
  for item in target[1:]:
    if item < smallest:
      smallest = item
  return smallest

def sort(to_sort: list[int]) -> list[int]:
  copy = to_sort.copy()
  sorted = []
  while not len(copy) == 0:
    smallest = find_smallest_item(copy)
    sorted.append(smallest)
    copy.remove(smallest)
  return sorted

if __name__ == '__main__':
  print(sort([3, 6, 2, 7, 4]))