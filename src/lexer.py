from src.lib.lib import Reserved, Token, Type

class Lexer:

  @staticmethod
  def from_file(file_name):
    f = open(file_name, 'r')
    lexer = Lexer(f.read())
    f.close()
    return lexer

  def __init__(self, text):
    self.reserved = Reserved()
    self.pos = 0
    self.text = text

  def get_next_token(self):

    while self.pos < len(self.text) and self.text[self.pos].isspace():
      self.pos += 1

    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '//':
      self.pos += 2
      while self.pos < len(self.text) and self.text[self.pos] != '\n':
        self.pos += 1
      while self.pos < len(self.text) and self.text[self.pos].isspace():
        self.pos += 1
    
    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '/*':
      self.pos += 2
      while self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] != '*/':
        self.pos += 1
      while self.pos < len(self.text) and self.text[self.pos].isspace():
        self.pos += 1

    if self.pos == len(self.text):
      return Token(Type.EOF, '')

    if self.text[self.pos].isalpha() and not self.text[self.pos].isdigit():
      i = self.pos
      while self.pos < len(self.text) and self.text[self.pos].isalpha() and not self.text[self.pos].isdigit():
        self.pos += 1
      while self.pos < len(self.text) and self.text[self.pos] == '`':
        self.pos += 1
      lexeme = self.text[i:self.pos]
      if lexeme in self.reserved.words:
        return self.reserved.words[lexeme]
      return Token(Type.ID, self.text[i:self.pos])

    if self.text[self.pos] == '"':
      self.pos += 1
      i = self.pos
      while self.pos < len(self.text) and self.text[self.pos] != '"':
        self.pos += 1
      if self.pos == len(self.text):
        raise
      j = self.pos
      self.pos += 1
      return Token(Type.STRING, self.text[i:j])

    if self.text[self.pos] == "'":
      self.pos += 1
      i = self.pos
      while self.pos < len(self.text) and self.text[self.pos] != "'":
        self.pos += 1
      if self.pos == len(self.text):
        raise
      j = self.pos
      self.pos += 1
      return Token(Type.STRING, self.text[i:j])

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

    if self.text[self.pos] == '_':
      self.pos += 1
      return Token(Type.UNDER, '_')

    if self.pos+2 < len(self.text) and self.text[self.pos:self.pos+3] == '**T':
      self.pos += 3
      return Token(Type.TPOSE, '**T')

    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '**':
      self.pos += 2
      return Token(Type.POW, '**')
    
    if self.text[self.pos] == '*':
      self.pos += 1
      return Token(Type.COMPOSE, '*')

    if self.text[self.pos] == '/':
      self.pos += 1
      return Token(Type.DIV, '/')

    if self.text[self.pos] == '%':
      self.pos += 1
      return Token(Type.MOD, '%')
    
    if self.text[self.pos] == '^':
      self.pos += 1
      return Token(Type.XOR, '^')

    if self.text[self.pos] == '&':
      self.pos += 1
      return Token(Type.AND, '&')

    if self.text[self.pos] == '+':
      self.pos += 1
      return Token(Type.UNION, '+')

    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '->':
      self.pos += 2
      return Token(Type.TO, '->')

    if self.text[self.pos] == '-':
      self.pos += 1
      return Token(Type.DIFF, '-')

    if self.text[self.pos] == '#':
      self.pos += 1
      return Token(Type.CARD, '#')

    if self.text[self.pos] == '!':
      self.pos += 1
      return Token(Type.FACT, '!')

    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '~=':
      self.pos += 2
      return Token(Type.NEQ, '~=')
    
    if self.text[self.pos] == '~':
      self.pos += 1
      return Token(Type.NOT, '~')
    
    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '>=':
      self.pos += 2
      return Token(Type.GTEQ, '>=')
    
    if self.text[self.pos] == '>':
      self.pos += 1
      return Token(Type.GT, '>')

    if self.pos+2 < len(self.text) and self.text[self.pos:self.pos+3] == '<=>':
      self.pos += 3
      return Token(Type.IFF, '<=>')
    
    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '<=':
      self.pos += 2
      return Token(Type.LTEQ, '<=')
    
    if self.text[self.pos] == '<':
      self.pos += 1
      return Token(Type.LT, '<')
    
    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '=>':
      self.pos += 2
      return Token(Type.IMPL, '=>')

    if self.text[self.pos] == '=':
      self.pos += 1
      return Token(Type.EQ, '=')

    if self.text[self.pos] == '(':
      self.pos += 1
      return Token(Type.OPENP, '(')

    if self.text[self.pos] == ')':
      self.pos += 1
      return Token(Type.CLOSEP, ')')
    
    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '||':
      self.pos += 2
      return Token(Type.NORM, '||')

    if self.text[self.pos] == '|':
      self.pos += 1
      return Token(Type.PIPE, '|')

    if self.text[self.pos] == '[':
      self.pos += 1
      return Token(Type.OPENB, '[')

    if self.text[self.pos] == ']':
      self.pos += 1
      return Token(Type.CLOSEB, ']')
    
    if self.text[self.pos] == '{':
      self.pos += 1
      return Token(Type.OPENC, '{')

    if self.text[self.pos] == '}':
      self.pos += 1
      return Token(Type.CLOSEC, '}')

    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == ':=':
      self.pos += 2
      return Token(Type.DEFAS, ':=')
    
    if self.text[self.pos] == ':':
      self.pos += 1
      return Token(Type.COLON, ':')
    
    if self.pos+1 < len(self.text) and self.text[self.pos:self.pos+2] == '..':
      self.pos += 2
      return Token(Type.RANGE, '..')
    
    if self.text[self.pos] == '.':
      self.pos += 1
      return Token(Type.PERIOD, '.')
    
    if self.text[self.pos] == ',':
      self.pos += 1
      return Token(Type.COMMA, ',')
    
    if self.text[self.pos] == ';':
      self.pos += 1
      return Token(Type.SEMIC, ';')

    if self.text[self.pos] == '?':
      self.pos += 1
      return Token(Type.QUEST, '?')

    raise
