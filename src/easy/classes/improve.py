# Mach es doch besser! (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/klassen/003/)
class Disk:
  def __init__(self, size: int):
    self.size: int = size

  def __str__(self) -> str:
    # Print two * so the hierarchy becomes clear.
    return '**' * self.size

  def __int__(self) -> int:
    return self.size


class Rod:
  def __init__(self):
    self.disks: list[Disk] = []

  def __len__(self) -> int:
    return len(self.disks)

  def __int__(self) -> int:
    if len(self) > 0:
      return self.disks[-1].size

  def may_place(self, disk: Disk) -> bool:
    return len(self) == 0 or int(self) > disk.size

  def place(self, disk: Disk) -> None:
    if not self.may_place(disk):
      return
    self.disks.append(disk)

  def top(self) -> Disk | None:
    return self.disks[-1]

  # Note: This design is stupid, but enforced by the assignment.
  def pop(self) -> Disk:
    """
    Remove the disk at the top of the rod
    """
    return self.disks.pop()


class Board:
  def __init__(self, disks_number: int):
    self.disks_number: int = disks_number
    self.rods = [Rod(), Rod(), Rod()]
    for index in range(0, disks_number):
      self.rods[0].place(Disk(disks_number - index))

  def is_move_valid(self, from_rod: int, to_rod: int) -> bool:
    if len(self.rods[from_rod]) == 0:
      return False
    return self.rods[to_rod].may_place(self.rods[from_rod].top())

  def move_disk(self, from_rod: int, to_rod: int) -> bool:
    if not (0 <= from_rod < 3 and 0 <= to_rod < 3):
      return False
    if not self.is_move_valid(from_rod, to_rod):
      return False

    disk = self.rods[from_rod].pop()
    self.rods[to_rod].place(disk)
    return True

  def has_finished(self):
    return len(self.rods[-1]) == self.disks_number

  def __str__(self) -> str:
    builder = ""
    for line in range(1, self.disks_number + 1):
      for rod in self.rods:
        rod_index = self.disks_number - line
        if len(rod) > rod_index:
          # Here you can see, why this design is stupid.
          # We still have to access the internal 'disks' list.
          builder = builder + (
            "." * (self.disks_number - int(rod.disks[rod_index]))
            + str(rod.disks[rod_index])
            + "." * (self.disks_number - int(rod.disks[rod_index]))
          )
        else:
          builder = builder + "." * (2 * self.disks_number)
        builder = builder + "|"
      builder = builder + '\n'

    return builder


# Smallest solution for board with 3 disks:
#
# board = Board(3)
# board.move_disk(0, 2)
# board.move_disk(0, 1)
# board.move_disk(2, 1)
# board.move_disk(0, 2)
# board.move_disk(1, 0)
# board.move_disk(1, 2)
# board.move_disk(0, 2)
def hanoi():
  board = Board(3)
  print(f"{board}")

if __name__ == '__main__':
  hanoi()
