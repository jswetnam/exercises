 # Given a list of 32-bit ints, write a function that takes the list and
 # returns true if a number appears more than once, false otherwise.

 # Examples:
 # f([1,2,3]) -> False
 # f([1,2,3,1]) -> True

 # Phone interview on 2/13/2013

 # A couple minor syntax erros on this one, but overall I did well.
 # My procedure is O(n) time and O(n) memory.

 # Tags: hashtable

import collections

def ContainsDuplicates(list):
  """ Return true if the given list contains at least one duplicate, false otherwise."""
  counts = collections.defaultdict(lambda: 0)
  for num in list:
    if counts[num]:
      return True
    else:
      counts[num] += 1

  return False

def main():
  no_duplicates  = [1, 2, 3, 4, 5]
  print no_duplicates
  print "ContainsDuplicates: " + str(ContainsDuplicates(no_duplicates))
  duplicates = [1, 2, 3, 4, 1 ]
  print duplicates
  print "ContainsDuplicates: " + str(ContainsDuplicates(duplicates))

if __name__ == "__main__":
  main()

