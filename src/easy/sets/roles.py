# Rollen vergeben (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-100/sets/001/)
available_roles_list = ["everyone", "Mitglied", "Ersti", "gaming", "memes", "LuDS", "TI", "ItSi", "SusProg"]

if __name__ == '__main__':
  available_roles_set = set(available_roles_list)

  for role in available_roles_set:
    print(role)

  available_roles_set.add('AlPro')
  print(available_roles_set)

  existing = {"everyone", "Mitglied", "AlPro", "LuDS"}
  modified = {"everyone", "Mitglied", "AlPro", "LuDS", "TI"}
  diff = set(modified).difference(existing)
  print(diff)

  existing = {"everyone", "Mitglied", "Ersti", "AlPro"}
  modified = {"everyone", "Mitglied", "AlPro", "LuDS", "TI"}
  to_add = set(modified).difference(existing)
  to_remove = set(existing).difference(modified)
  print(to_add)
  print(to_remove)

  existing = {"everyone", "Mitglied", "Ersti"}
  print(set(available_roles_list).difference(existing))

  print('Oatly' in available_roles_list)