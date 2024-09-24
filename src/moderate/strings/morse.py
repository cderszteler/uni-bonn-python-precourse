# Finger vom Lichtschalter (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/strings/002/)
morse_alphabet = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
  'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
  '4': '....-', '5': '.....', '6': '-....', '7': '--...',
  '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
  '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
  '(': '-.--.', ')': '-.--.-'
}
reverse_morse_alphabet = {value: key for key, value in morse_alphabet.items()}

def encrypt(text: str) -> str:
  code = []
  for character in text.upper():
    morse = morse_alphabet.get(character, character)
    if morse == character:
      print(f'Could not find morse for {character} character.')
    code.append(morse)
  return ' '.join(code)

def decrypt(morse: str) -> str:
  text = ""
  for code in morse.split(' '):
    character = reverse_morse_alphabet.get(code, code)
    if code == character:
      print(f'Could not find character for {code} code.')
    text += character
  return text

def main():
  print(encrypt('CYBER'))
  print(decrypt(encrypt('CYBER')))

if __name__ == '__main__':
  main()