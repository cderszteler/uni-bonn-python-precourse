# Einladendes E-Campus (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/klassen/005/)
from functools import total_ordering


@total_ordering
class Student:
  def __init__(self, matriculation_number: int, firstname: str, lastname: str):
    self.matriculation_number = matriculation_number
    self.firstname = firstname
    self.lastname = lastname

  def __eq__(self, student) -> bool:
    return (
      (self.lastname.lower(), self.firstname.lower(), self.matriculation_number) ==
      (student.lastname.lower(), student.firstname.lower(), student.matriculation_number)
    )

  def __lt__(self, student) -> bool:
    return (
      (self.lastname.lower(), self.firstname.lower(), self.matriculation_number) <
      (student.lastname.lower(), student.firstname.lower(), student.matriculation_number)
    )

  def __str__(self) -> str:
    return (
      'Student('
      f'matriculation_number={{{self.matriculation_number}}}, '
      f'firstname={{{self.firstname}}}, '
      f'lastname={{{self.lastname}}}'
    )

  def __repr__(self) -> str:
    return self.__str__()

class Course:
  def __init__(self, name: str, participants: list[Student], lecturers: list[Student]):
    self.name = name
    self.participants = participants
    self.lecturers = lecturers

  def add_student(self, student: Student) -> None:
    self.participants.append(student)

  def add_lecturer(self, lecturer: Student) -> None:
    self.lecturers.append(lecturer)

  def list_students(self) -> list[Student]:
    return self.participants

  def list_lecturers(self) -> list[Student]:
    return self.lecturers

  def __len__(self) -> int:
    return len(self.participants)

  def __contains__(self, student: Student) -> bool:
    return student in self.participants or student in self.lecturers

  def __eq__(self, comparison) -> bool:
    return self.name.lower() == comparison.name.lower()

  def __ne__(self, other) -> bool:
    return not self.__eq__(other)

  def __str__(self) -> str:
    return f'{self.name} with {self.lecturers}'

if __name__ == '__main__':
  course = Course("Python Vorkurs", [], [])
  course.add_student(Student(1, 'Joe', 'Mama'))
  course.add_student(Student(2, 'Max', 'Musterer'))
  course.add_lecturer(Student(3, 'Pidser', 'König'))
  print(f'Students: {course.list_students()} ({len(course)})')
  print(course)