# Calculates the sum of 1 to n (1 + 2 + ... + n)
def func(n: int):
  if n == 0:
    return 0
  return n + func(n-1)