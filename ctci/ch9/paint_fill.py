# CTCI 9.6 Implement the "paint fill" function that one might see on many
# image editing programs.  That is, given a screen (2D array of colors),
# a point, and a new color, fill in the surrounding area until the color
# changes from the original color.


def PaintFill(image, x, y, orig_color, new_color):
  if not (0 < x and x < len(image)):
    return
  if not (0 < y and y < len(image[0])):
    return
  if image[x][y] != orig_color or image[x][y] == new_color:
    return
  else:
    image[x][y] = new_color
    PaintFill(image, x + 1, y, orig_color, new_color) # Right
    PaintFill(image, x - 1, y, orig_color, new_color) # Left
    PaintFill(image, x, y + 1, orig_color, new_color) # Up
    PaintFill(image, x, y - 1, orig_color, new_color) # Down

IMAGE = """*******
***###*
**##*#*
*##)##*
****)))"""

def MatrixFromImage(img):
  row_strings = img.split('\n')
  rows = []
  for row in row_strings:
    rows.append([value for value in row])

  return rows

def ImageFromMatrix(matrix):
  return "\n".join(["".join(col for col in matrix[i]) for i in range(len(matrix))])

def main():
  print IMAGE
  img = MatrixFromImage(IMAGE)
  import pdb; pdb.set_trace()
  PaintFill(img, 2, 3, '#', '*')
  print "-----------------------------"
  print ImageFromMatrix(img)

if __name__ == '__main__':
  main()
