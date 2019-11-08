from math import floor, sqrt
from util import Queue
from LineReader import LineReader
# import numpy as np
# from scipy.ndimage.measurements import center_of_mass
from copy import deepcopy

def fill(matrix, color, center):
  queue = Queue()
  queue.push(center)
  steps = [(1, 0), (0, -1), (0, 1), (-1, 0)]
  explored = set([center])

  while not queue.isEmpty():
    curr = queue.pop()
    x, y = curr
    if matrix[x][y] == color:
      if matrix[x - 1][y] == color and matrix[x + 1][y] == color and matrix[x][y - 1] == color and matrix[x][y + 1] == color:
        # inside, not on border
        return curr
    for step in steps:
      dx, dy = step
      x_ = (x + dx, y + dy)
      if x_ not in explored:
        queue.push(x_)
        explored.add(x_)

  return None

def euclid(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def sebi(matrix, rows, cols, color, center):
  best = (1e10, 1e10)
  for x in range(rows):
    for y in range(cols):
      if x == 0 or y == 0: continue
      if x == rows - 1 or y == cols - 1: continue
      if matrix[x][y] == color:
        if matrix[x - 1][y] == color and matrix[x + 1][y] == color and matrix[x][y - 1] == color and matrix[x][y + 1] == color:
          # inside, not on border
          dist = euclid(center, (x, y))
          dist_2 = euclid(center, best)
          if dist < dist_2:
            best = (x, y)
          elif dist == dist_2:
            if x < best[0]:
              best = (x, y)
            elif x == best[0] and y < best[1]:
              best = (x, y)
  return best

if __name__ == "__main__":
  level = 3
  levels = [("level%d/level%d_%d.in" % (level, level, i), "out/level%d/%d.out" % (level, i)) for i in range(5, 6)] 

  for (fin, fout) in levels:
    reader = LineReader(fin)
    [rows, cols] = reader.readline('i')
    f = open(fin, 'r')
    matrix = []
    for line in list(f)[1:]:
      line = [int(x) for x in line.split(' ')]
      line = line[1::2]
      matrix.append(line)
    d = {}
    for row in range(rows):
      for col in range(cols):
        color = matrix[row][col]
        item = (row, col)
        if color in d:
          d[color].append(item)
        else:
          d[color] = [item]
    avg = {}
    for color, items in d.items():
      x, y = 0, 0
      for item in items:
        x += item[0]
        y += item[1]
      size = len(items)
      x = int(floor(x / size))
      y = int(floor(y / size))
      avg[color] = (x, y)
      # print(avg[color])
      #print(fin, 'Ours:', avg[color])
      # curr = deepcopy(matrix)
      # curr = [[0] * len(row) for row in matrix]
      # for pos in d[color]:
      #   x, y = pos
      #   curr[x][y] = 1
      # curr = np.array(curr)
      # center = center_of_mass(curr)
      # print(fin, 'Theirs:', center)


    f = open(fout, 'w')
    for color in sorted(avg.keys()):
      x, y = sebi(matrix, rows, cols, color, avg[color])
      f.write('%d %d\n' % (y, x))
      # f.write('%d\n' % (d[i],))