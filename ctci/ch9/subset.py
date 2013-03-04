# CTCI 9.4 Write a function to find all subsets of a set.

def FindSubsets(of_set):
  """Returns a list of sets, all of the subsets of the given set."""
  if len(of_set) == 0:
    return [[]]
  else:
    without_first = FindSubsets(of_set[1:])
    subsets = []
    for subset in without_first:
      subsets.append([of_set[0]] + subset)
    subsets.extend(without_first)
    return subsets

def main():
  test_set = [1, 2, 3]
  for subset in FindSubsets(test_set):
    print subset

if __name__ == '__main__':
  main()

