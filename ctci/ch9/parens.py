# CTCI 9.6 Implement an algorithm to print all valid (e.g. properly opened and closed) combinations
# of n-pairs of parentheses.

# 1 : ()
# 2 : ()() (())

def PrintParens(N):
  assert N >= 0
  if not N:
    yield ''
  elif N == 1:
    yield '()'
  else:
    for sub_paren in PrintParens(N - 1):
      yield '(' + sub_paren + ')'
      yield '()' + sub_paren
      yield  sub_paren + '()'


def main():
  print "PrintParens(1) "
  for paren in PrintParens(1):
    print paren
  print "PrintParens(2) "
  for paren in PrintParens(2):
    print paren
  print "PrintParens(3) "
  for paren in PrintParens(3):
    print paren

if __name__ == '__main__':
  main()
