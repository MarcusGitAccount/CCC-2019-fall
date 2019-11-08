from LineReader import LineReader

if __name__ == "__main__":
  level = 1
  levels = [("level%d/level%d_%d.in" % (level, level, i), "out/level%d/%d.out" % (level, i)) for i in range(1, 6)] 

  filename = 'file'
  try:
    reader = LineReader(filename) 
    print(reader.read_matrix(3, 3, 'i'))
  except Exception:
    print('Couldn\'t create line reader.')