# CTCI 1.3 Given two strings, write a function to decide if one string
# is a permutation of another.


import collections

def IsPermutation(a, b):
  """Return true if string a is a permutation of string b, false otherwise."""
  a_ct = collections.Counter(a)
  b_ct = collections.Counter(b)

  for char, value in a_ct.items():
    if char not in b_ct or a_ct[char] != b_ct[char]:
      return False

  return True


def main():
  a = "abcde"
  b = "bcaed"
  print "String A: " + a
  print "String B: " + b

  print "IsPermutation(a, b): " + str(IsPermutation(a, b))

  a = "cat"
  b = "dog"
  print "String A: " + a
  print "String B: " + b

  print "IsPermutation(a, b): " + str(IsPermutation(a, b))



if __name__ == "__main__":
  main()



