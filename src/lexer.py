from src.lib.lib import Token, Type

class Lexer:

  @staticmethod
  def from_file(file_name):
    f = open(file_name, 'r')
    lexer = Lexer(f.read())
    f.close()
    return lexer

  def __init__(self, text):
    self.text = text
    self.pos = 0

  def get_next_token(self):

    while self.pos < len(self.text) and self.text[self.pos].isspace():
      self.pos += 1

    while self.pos < len(self.text) and self.text[self.pos] == '#':
      while self.pos < len(self.text) and self.text[self.pos] != '\n':
        self.pos += 1
      while self.pos < len(self.text) and self.text[self.pos].isspace():
        self.pos += 1

    if self.pos == len(self.text):
      return Token(Type.EOF, '')

    if self.text[self.pos] == '0':
      i = self.pos
      self.pos += 1
      if not (self.pos < len(self.text) and self.text[self.pos] == '.'):
        return Token(Type.INT, int(self.text[i]))
      self.pos += 1
      if not(self.pos < len(self.text) and self.text[self.pos] >= '0' and self.text[self.pos] <= '9'):
        raise
      while self.pos < len(self.text) and self.text[self.pos] >= '0' and self.text[self.pos] <= '9':
        self.pos += 1
      return Token(Type.REAL, float(self.text[i:self.pos]))

    if self.text[self.pos] >= '1' and self.text[self.pos] <= '9':
      i = self.pos
      while self.pos < len(self.text) and self.text[self.pos] >= '0' and self.text[self.pos] <= '9':
        self.pos += 1
      if not (self.pos < len(self.text) and self.text[self.pos] == '.'):
        return Token(Type.INT, int(self.text[i:self.pos]))
      self.pos += 1
      if not(self.pos < len(self.text) and self.text[self.pos] >= '0' and self.text[self.pos] <= '9'):
        raise
      while self.pos < len(self.text) and self.text[self.pos] >= '0' and self.text[self.pos] <= '9':
        self.pos += 1
      return Token(Type.REAL, float(self.text[i:self.pos]))

    if self.text[self.pos] == '*':
      self.pos += 1
      if self.pos < len(self.text) and self.text[self.pos] == '*':
        self.pos += 1
        return Token(Type.POW, '**')
      return Token(Type.DOT, '*')

    if self.text[self.pos] == '/':
      self.pos += 1
      return Token(Type.DIV, '/')

    if self.text[self.pos] == '%':
      self.pos += 1
      return Token(Type.MOD, '%')

    if self.text[self.pos] == '+':
      self.pos += 1
      return Token(Type.PLUS, '+')

    if self.text[self.pos] == '-':
      self.pos += 1
      return Token(Type.MINUS, '-')

    if self.text[self.pos] == '!':
      self.pos += 1
      return Token(Type.FACT, '!')

    if self.text[self.pos] == '(':
      self.pos += 1
      return Token(Type.OPENP, '(')

    if self.text[self.pos] == ')':
      self.pos += 1
      return Token(Type.CLOSEP, ')')

    if self.text[self.pos] == '|':
      self.pos += 1
      return Token(Type.PIPE, '|')

    raise
