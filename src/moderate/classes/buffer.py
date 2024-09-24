# Ring der Macht (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/classes/004/)
from typing import Any, Optional


class RingBuffer:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.items = []
    pass

  def push(self, element: Any):
    if len(self.items) >= self.capacity:
      del self.items[0]
    self.items.append(element)

  def pop(self) -> Optional[Any]:
    if len(self.items) == 0:
      return None
    element = self.items[0]
    del self.items[0]
    return element

  def peek(self) -> Optional[Any]:
    if len(self.items) == 0:
      return None
    return self.items[0]

  def __len__(self) -> int:
    return len(self.items)


def test():
  # Test normal operation without overwrites
  buffer = RingBuffer(3)
  assert buffer.capacity == 3
  assert len(buffer) == 0
  buffer.push(1)
  buffer.push(3)
  buffer.push(4)
  assert buffer.peek() == 1
  assert len(buffer) == 3
  assert buffer.pop() == 1
  assert buffer.pop() == 3
  assert buffer.pop() == 4
  assert buffer.pop() is None

  # Test operation with overwrites
  buffer.push(10)
  buffer.push(20)
  buffer.push(30)
  buffer.push(40)
  buffer.push(50)
  assert buffer.pop() == 30
  assert buffer.pop() == 40
  assert buffer.pop() == 50
  assert buffer.pop() is None


if __name__ == "__main__":
  test()
