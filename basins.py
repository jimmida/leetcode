class Solution:
  def __init__(self):
    self.group      = 0
    self.assigned   = None
    self.unassgined = None

  def main(self, A, m):
    self.assigned = [[0]*m]*m
    pass

  def process_land(self, A, x, y):
    global processed

    land   = (x, y)
    top    = (x, y-1)
    bottom = (x, y+1)
    left   = (x-1, y)
    right  = (x+1, y)

    cells = [land, top, bottom, left, right]

    heights = {}
    for cell in cells:
      (a,b) = cell
      heights[cell] = A[a][b]

    if heights[land] < min([list(set(heights.values()) - set([heights[land]]))]):
      self.group += 1
      self.assigned[x][y]   = self.group
      self.assigned[x][y-1] = self.group
      self.assigned[x][y+1] = self.group
      self.assigned[x-1][y] = self.group
      self.assigned[x+1][y] = self.group




# Input:
# 3
# 1 5 2
# 2 4 7
# 3 6 9

# Output:
# 7 2
# The basins, labeled with A’s and B’s, are:
# A A B
# A A B
# A A A
# -------------------------------
# Input:
# 5
# 1 0 2 5 8
# 2 3 4 7 9
# 3 5 7 8 9
# 1 2 5 4 2
# 3 3 5 2 1

# Output:
# 11 7 7

# The basins, labeled with A’s, B’s, and C’s, are:
# A A A A A
# A A A A A
# B B A C C
# B B B C C
# B B C C C
# -------------------------------
# Input:
# 4
# 0 2 1 3
# 2 1 0 4
# 3 3 3 3
# 5 5 2 1

# Output:
# 7 5 4

# A A B B
# A B B B
# A B B C
# A C C C