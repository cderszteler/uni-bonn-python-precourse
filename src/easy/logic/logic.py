# Ist doch logisch? (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/logik/001/)
if __name__ == '__main__':
  types = ["feuer", "wasser", "pflanze"]
  count = 3
  attack = 5.5
  favorite = {
    "name": "Glumanda", "typ": types[0], "angriff": attack,
    "schrei": "glumanda!", "leben": 200
  }

  if favorite['name'] == 'Shiggy':
    print(1)
  if attack > 3:
    print(2)
  if 'boden' in types:
    print(3)
  if favorite['leben'] is None:
    print(4)
  if isinstance(attack, int):
    print(5)
  if type(count) == type(types):
    print(6)
  if len(favorite.keys()) > 8:
    print(7)
  if len(favorite['schrei']) > 4:
    print(8)
  if favorite['schrei'].endswith('?'):
    print(9)

  types = ["feuer", "wasser", "pflanze"]
  glumanda = {"name": "Glumanda", "typ": types[0], "angriff": 5.5, "abwehr": 3, "schrei": "glumanda!", "leben": 200}
  shiggy = {"name": "Shiggy", "typ": types[1], "angriff": 3.5, "abwehr": 5, "schrei": "shiggy!", "leben": 150}

  if shiggy['typ'] == 'wasser' and glumanda['typ'] == 'feuer':
    print(1)
  if shiggy['angriff'] > glumanda['angriff'] or shiggy['abwehr'] > glumanda['abwehr']:
    print(2)
  if (
    (isinstance(shiggy['abwehr'], int) and isinstance(shiggy['angriff'], float))
    or len(types) > 3
  ):
    print(3)
  if len(shiggy.keys()) == len(glumanda.keys()) and len(shiggy.keys()) < len(types):
    print(4)
  if shiggy['typ'] in types and glumanda['typ'] in types:
    print(5)
  if shiggy['leben'] > shiggy['abwehr'] > shiggy['angriff']:
    print(6)