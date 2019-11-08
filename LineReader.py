import os, re

class LineReader:
  parsers = {
    'i': int,
    'f': float,
    's': str
  }

  def __init__(self, path):
    if not os.path.exists(path):
      raise Exception('File %s does not exist' % path) 
    self.path = path
    self._index = 0
    self.fp = open(self.path, 'r')
    self.splitter = re.compile(r'[\s]+')
    self.can_read = True

  # @param format: parsers for each @count elements or general parser for all
  #                elements if character
  # @param whole: if True will simply return the whole line as a string
  # @param count: how many variables will be read. If None, the number will be 
  #               determined using the format length
  def readline(self, format, whole = False, count = None):
    if not self.can_read:
      return None
    self._index += 1
    line = self.fp.readline().rstrip('\n\r') # read and remove trailing chars
    
    if line is None:
      self.can_read = False
      self.fp.close()
      return None
    if whole:
      # return the whole line
      return line
    
    assert isinstance(format, str), 'Wrong format for parsers'
    format = format.replace(' ', '')
    assert len(format) >= 1

    elements = self.splitter.split(line)
    elements = list(filter(None, elements)) # remove empty strings
    facade = None
    for parser in format:
      assert parser in LineReader.parsers, 'Parser %s doest no exist' % parser

    size = 0
    if len(format) > 1:
      assert len(format) >= len(format), 'Too many parsers where given'
      facade = lambda index: LineReader.parsers[format[index]]
      size = count or len(format)
    else:
      facade = lambda index: LineReader.parsers[format[0]]
      size = count or len(elements)
    return [facade(index)(elements[index]) for index in range(size)]

  def read_matrix(self, rows, cols, format):
    if not self.can_read:
      return None
    format = ''.join([format for i in range(cols)])
    result = []

    row = 0
    while row < rows:
      result.append(self.readline(format, count=cols))
      row += 1
    return result

  def close(self):
    if self.fp:
      self.fp.close()

if __name__ == '__main__':
  filename = 'file'
  try:
    reader = LineReader(filename) 
    print(reader.readline('i'))
    print(reader.readline('i s'))
    print(reader.readline('f f s'))
    print(reader.readline('i', whole=True))
    print(reader.read_matrix(3, 1, 'i'))
    print(reader.readline('s'))
  except Exception:
    print('Couldn\'t create line reader.')