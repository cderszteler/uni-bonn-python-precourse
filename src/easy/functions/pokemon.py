# Func func func (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/funktionen/001/)
def type_of_pokemon(pokemon: dict, multiple = False) -> (str, str | list[str] | None):
  """
  Diese Methode gibt anhand eines Pokemons, repräsentiert in einem dict, seinen Namen und sein Typ zurück.
  Besitzt das Pokemon kein Typ, dann wird None als 2. Parameter zurückgegeben.
  Besitzt das Pokemon mehrere Typen, werden diese mit ', ' gejoined und als String zurückgegeben.
  :param pokemon: Das Pokemon repräsentiert mittels eines dicts
  :param multiple: Bool, ob das Pokemon mehrere Typen besitzt (type(pokemon['typ']) == list)
  :return: In einem Tupel, 1. Name des Pokemons, 2. Typ des Pokemons (ggf. gejoined mit ', ')
  """
  if 'typ' not in pokemon:
    return pokemon['name'], None
  if multiple:
    return pokemon['name'], ', '.join(pokemon['typ'])
  return pokemon['name'], pokemon['typ']