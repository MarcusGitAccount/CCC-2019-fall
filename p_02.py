from LineReader import LineReader
if __name__ == "__main__":
  level = 2
  levels = [("level%d/level%d_%d.in" % (level, level, i), "out/level%d/%d.out" % (level, i)) for i in range(1, 6)] 

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
        if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
          if color in d:
            d[color] += 1
          else:
            d[color] = 1
        elif color != matrix[row - 1][col] or color != matrix[row + 1][col] or color != matrix[row][col - 1] or color != matrix[row][col + 1]:
          if color in d:
            d[color] += 1
          else:
            d[color] = 1
    f = open(fout, 'w')
    for i in range(len(d.keys())):
      f.write('%d\n' % (d[i],))