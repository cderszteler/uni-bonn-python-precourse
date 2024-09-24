# Happy Cyber-Chris noises (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/type-hinting/001/)
var_1: int = 42
var_2: float = 1.5
var_3: str = "das ist ein string!"
var_4: bool = False

cool_list: list[int] = [1, 2, 3]
cool_dict: dict[int, str] = {42: "Die Antwort auf die Frage nach dem Leben, dem Universum und dem ganzen Rest"}

mega_cool_dict: dict[int, list[int]] = {1: cool_list}

def was_gebe_ich_wohl_zurueck(text: str, number: int, char: str) -> str:
  return text + number * char

def main() -> int:
  print(was_gebe_ich_wohl_zurueck("python goes b", 10, 'r'))
  return 0

if __name__ == "__main__":
  main()
