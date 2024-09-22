# yranoitciD (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/dictionaries/005/)
grades = {
  'sehr gut': '1',
  'gut': '2',
  'befriedigend': '3',
  'ausreichend': '4',
  'mangelhaft': '5',
  'ungenügend': '6'
}

def reverse_dict(dictionary: dict[any, any]) -> dict[any, any]:
  reversed_dict = {}
  for key, value in dictionary.items():
    reversed_dict[value] = key
  return reversed_dict

if __name__ == '__main__':
  reversed_grades = reverse_dict(grades)
  grade = input('Bitte gib eine Schulnote ein: ')
  written_grade = reversed_grades.get(grade)
  if written_grade is not None:
    print(written_grade)
    if int(grade) != 1:
      print(reversed_grades[str(int(grade) - 1)])
  else:
    print('Diese Schulnote existiert nicht!')
