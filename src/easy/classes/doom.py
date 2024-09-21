# DOOM (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/klassen/002/)

class Entity:
  def __init__(self, name: str, health: int, power: int):
    self.name = name
    self.health = health
    self.power = power

  def receive_damage(self, damage: int) -> None:
    self.health -= damage

class Player(Entity):
  def __init__(self, name: str):
    super().__init__(name, 3, 1)
    self.name = name
    self.level = 1

  def level_up(self) -> None:
    self.level += 1

class Monster(Entity):
  def __init__(self, name: str, health: int, power: int):
    super().__init__(name, health, power)

  def rage(self, activate: bool) -> None:
    if self.power % 2 != 0:
      raise ValueError('rage must be activated first')
    self.power = self.power * 2 if activate else self.power / 2