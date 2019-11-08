from math import floor, sqrt
from util import Queue
from LineReader import LineReader
# import numpy as np
# from scipy.ndimage.measurements import center_of_mass
from copy import deepcopy

def next_point(curr, dir, eps=1e-5):
  x, y = curr
  dx, dy = dir
  return (x + eps * dx, y + eps * dy)

if __name__ == "__main__":
  level = 4
  levels = list()
  levels = [("level%d/level%d_%d.in" % (level, level, i), "out/level%d/%d.out" % (level, i)) for i in range(2, 3)] 
  # levels.append(('level4/level4_example.in', 'out/level4/level4_example.out'))
  for (fin, fout) in levels:
    reader = LineReader(fin)
    [rows, cols] = reader.readline('i')
    [n] = reader.readline('i')
    f = open(fout, 'w')
    for i in range(n):
      # query i
      eps = 3 * 1e-5
      x, y, dx, dy = reader.readline('i')
      origin = (x, y)
      size = sqrt(dx * dx + dy * dy)
      dir = (dx / size, dy / size)
      curr = origin
      sol = [curr]
      explored = set(sol)

      dominant = 'x'
      if abs(dx) < abs(dy):
        dominant = 'y'
      while True:
        curr = next_point(curr, dir, eps)
        x, y = curr
        x = int(floor(x + .5))
        y = int(floor(y + .5))
        if x < 0 or y < 0: break
        if x >= rows or y >= cols: break
        pos = (x, y)
        if pos not in explored:
          if len(sol) > 0:
            # diagonal shenigans
            prev = sol[-1]
            if abs(prev[0] - pos[0]) == 1 and abs(prev[1] - pos[1]) == 1:
              if dominant == 'x': # horizontan movement
                sol.append((pos[0], prev[1]))
                sol.append((prev[0], pos[1]))
              else:
                sol.append((prev[0], pos[1]))
                sol.append((pos[0], prev[1]))
          explored.add(pos)
          sol.append(pos)

      solution = ' '.join(['%d %d' % (x[0], x[1]) for x in sol])
      f.write('%s\n' % (solution,))
      print('fututi', i, n)