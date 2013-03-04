# CTCI 9.5 Write a method to compute all permutations of a string.

def FindPermutationsAux(string, permutation, permutations):
  if not string:
    permutations.append(permutation)
  else:
    for i in range(len(string)):
      FindPermutationsAux(string[:i] + string[i + 1:],
          permutation + string[i],
          permutations)

def FindPermutations(string):
  permutations = []
  FindPermutationsAux(string, "", permutations)
  return permutations

def main():
  for permutation in FindPermutations("abcde"):
    print permutation


if __name__ == '__main__':
  main()
