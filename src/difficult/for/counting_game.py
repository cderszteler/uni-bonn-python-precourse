# Mastermind (https://itsec.cs.uni-bonn.de/vorkurs/aufgaben-fuer-500/for-loops/001/)
import random


def evaluate_guess(number_digits: list[int], guess: int) -> (int, int):
  digits = split_int_into_digits(guess)
  identical = 0
  position = 0
  for index in range(len(digits)):
    digit = digits[index]
    if number_digits[index] == digit:
      identical += 1
    elif digit in number_digits:
      position += 1
  return identical, position


def take_guess() -> int:
  input_guess = None
  while input_guess is None:
    input_value = input('Guess a number between 0 and 9999: ')
    if input_value.isdigit() and (0 <= int(input_value) <= 9999):
      input_guess = int(input_value)
    else:
      print('Please enter a number between 0 and 9999.')
  return input_guess

def split_int_into_digits(number: int) -> list[int]:
  digits = [int(char) for char in str(number)]
  while len(digits) < 4:
    digits.insert(0, 0)
  return digits

def main():
  number = random.randint(0, 9999)
  number_digits = split_int_into_digits(number)
  tries = 1
  guess = -1
  while guess != number:
    guess = take_guess()
    if guess == number:
      print(
        f'You correctly guessed the number '
        f'{''.join([str(digit) for digit in number_digits])} in {tries} tries.'
        f' Congratulations!'
      )
      break
    identical, position = evaluate_guess(number_digits, guess)

    print(f'{identical} digits are already identical and ontop {position} digits\' position need to be changed.')
    tries += 1

if __name__ == '__main__':
  main()