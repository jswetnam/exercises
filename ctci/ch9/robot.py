# CTCI 9.2:
# Imagine a robot sitting in the upper left corner of an X by Y grid.
# The robot can only move in two directions: right and down.  How many
# possible paths are there for the robot to go from (0, 0) to (X, Y)?

# Imagine that certain spots are off-limits. Design an algorithm for the
# robot to go from the top left to the bottom right.

IMPASSIBLE = -1

def FindPath(M, x, y):
  """Return string representation of the path from 0, 0 to x, y in the 2D matrix
  M to the list path. Impassable cells have the value -1.  Returns None if no paths
  exist to 0, 0 from this point."""
  if (x, y) == (0, 0):
    return "S"
  else:
    if x - 1 >= 0 and M[x - 1][y] != IMPASSIBLE:
      path_left = FindPath(M, x - 1, y)
      if path_left: return path_left + "R"
    if y - 1 >= 0 and M[x][y - 1] != IMPASSIBLE:
      path_up = FindPath(M, x, y - 1)
      if path_up: return path_up + "D"


# M = [0][0]
#     [0][0]
# FindPath(M, 1, 1 "")
# FindPath(M, 0, 1 "")
# FindPath(M, 0, 0 "")
# D
# R

def PrintMatrix(M):
  for j in range(len(M)):
    row = ""
    for i in range(len(M[0])):
      row += "[%d] " % M[i][j]
    print row

def main():
  x, y = 5,5
  matrix = [[0 for _ in range(x)] for _ in range(y)]
  matrix[0][4] = IMPASSIBLE
  matrix[1][3] = IMPASSIBLE
  PrintMatrix(matrix)
#  import pdb; pdb.set_trace()
  print FindPath(matrix, 4, 4)


if __name__ == "__main__":
  main()

