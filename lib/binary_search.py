import random

def _BinarySearchAux(A, target, i, j):
  mid = (i + j) / 2
  if i == j:
    return None
  if A[mid] == target:
    return mid
  elif A[mid] > target:
    return _BinarySearchAux(A, target, mid + 1, j)
  elif A[mid] < target:
    return _BinarySearchAux(A, target, j, mid - 1)


def BinarySearch(A, target):
  """Search for the value target in the array A using binary search.

  Returns:
    index of target if found, None otherwise."""
  return _BinarySearchAux(A, target, 0, len(A))

if __name__ == '__main__':
  values = [random.randint(0, 10) for i in range(11)]
  values.insert(random.randint(0, len(values)), 5)

  values.sort()
  print values
  print BinarySearch(values, 5)

  values = [random.randint(0, 10) for i in range(11)]

  values.sort()
  print values
  print BinarySearch(values, 11)


