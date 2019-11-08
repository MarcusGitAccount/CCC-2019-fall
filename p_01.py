from LineReader import LineReader
import numpy as np

if __name__ == "__main__":
  level = 1
  levels = [("level%d/level%d_%d.in" % (level, level, i), "out/level%d/%d.out" % (level, i)) for i in range(1, 6)] 

  for (fin, fout) in levels:
    reader = LineReader(fin)
    [rows, cols] = reader.readline('i')
    matrix = reader.read_matrix(rows, cols, 'i')
    matrix = np.array(matrix)
    f = open(fout, "w")
    min_ = matrix.min()
    max_ = matrix.max()
    avg_ = np.floor(matrix.mean())
    # print(min_)
    f.write(str(min_) + ' ' + str(max_) + ' ' + str(int(avg_)))
