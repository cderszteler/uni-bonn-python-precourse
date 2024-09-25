# Seifenblasensortierer (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/for-loops/005/)

def bubble_sort(to_sort: list[int]) -> list[int]:
  sort_required = True
  while sort_required:
    sort_required = False
    for index in range(len(to_sort) - 1):
      first = to_sort[index]
      second = to_sort[index + 1]
      if first > second:
        to_sort[index] = second
        to_sort[index + 1] = first
        sort_required = True
  return to_sort

def main():
  print(bubble_sort([4,2,1,1,17,343,24,78]))

if __name__ == '__main__':
  main()