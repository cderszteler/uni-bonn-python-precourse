# Palindrom mordnilaP (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-200/strings/004/)
def check_palindrome(target: str, ignore_case=True) -> bool:
  modified = target.lower() if ignore_case else target
  return modified == modified[::-1]

def main():
  print(f"Checking 'Hannah': {check_palindrome('Hannah')}")
  print(f"Checking 'Hannah' (ignore_case=False): {check_palindrome('Hannah', ignore_case=False)}")
  print(f"Checking 'Palindrom': {check_palindrome('Palindrom')}")

if __name__ == '__main__':
  main()