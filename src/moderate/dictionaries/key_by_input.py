# Schlüssel durch input hinzufügen - Teil 2 (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/dictionaries/001/)
import builtins


def request_typed_input(request: str) -> any:
  input_value = input(request)
  wanted_type = input('Gib einen Typ ein: ')
  casted_type = getattr(builtins, wanted_type)(input_value)
  return casted_type

def request_typed_pair() -> (any, any):
  key = request_typed_input('Gib einen Key ein: ')
  value = request_typed_input('Gib ein Value ein: ')
  return key, value

if __name__ == '__main__':
  my_dict = {}
  for index in range(2):
    key, value = request_typed_pair()
    my_dict[key] = value
  print(f'Dictionary: {my_dict}')