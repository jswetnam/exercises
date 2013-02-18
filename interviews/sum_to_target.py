import random
# Given a list of 32-bit ints, and a target number, write a function that finds any
# two numbers from the list that sum to the target number. A number may be used twice.

# I had some difficulty with this one.  I easily came up with an O(n^2) solution, but
# was too flustered to remember to check whether I could use any relevant data structures
# to increase the efficiency.  Rookie mistake.  Lesson learned: stay calm and go through
# standard solution techniques.

# naive idea: test all n^2 combinations of two numbers from the list to see if they sum to target

def FindSumsToTarget(A, target):
  for x in A:
    for y in A:
      if x + y == target:
        return (x, y)

# I figured I could increase the efficiency by a factor of two by  only testing
# one half of the matrix since it is triangular.

def FindSumsToTargetTriangularMatrix(A, target):
  for i in range(0, len(A)):
    for j in range(0, i):
      if A[i] + A[j] == target: return (A[i], A[j])

# A better solution presents itself when we observe that this is in fact a search
# problem. For each integer  X the list, we are looking for a single integer y
# that, when added to X, will equal target.

# x + y = target
# y = target - x

# We can thus construct a hashtable and test for the presence of y:

def FindSumsToTargetHashtable(A, target):
  list_set = set(A)
  for x in A:
    y = (target - x)
    if y in list_set:
      return (x, y)

def main():
  test_data = [1, 2, 3, 4, 5]
#  for i in range(1, 1000):
#    test_data.append(random.randint(1, 1000000))
  print FindSumsToTarget(test_data, 6)
  print FindSumsToTargetTriangularMatrix(test_data, 6)
  print FindSumsToTargetHashtable(test_data, 6)

if __name__ == "__main__":
  main()

