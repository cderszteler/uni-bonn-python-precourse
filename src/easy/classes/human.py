# Wie entstehen neue Menschen? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/klassen/001/)
class Human:
  def __init__(self, name: str, birthdate: str, sex: str):
    self.name = name
    self.birthdate = birthdate
    self.sex = sex

  def introduce(self) -> None:
    print(f'Guten Tag, ich bin {self.name} ({self.sex}) und '
          f'ich wurde am {self.birthdate} geboren.')

  def __str__(self) -> str:
    return (
      f'Mensch{{name={{{self.name}}},'
      f' birthdate={{{self.birthdate}}},'
      f' sex={{{self.sex}}}}}'
    )