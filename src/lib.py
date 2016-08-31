class Type:
  CLOSEP, \
  DIV, \
  EOF, \
  FACT, \
  INT, \
  MOD, \
  MINUS, \
  MULT, \
  OPENP, \
  PIPE, \
  PLUS, \
  POW, \
  REAL = range(13)

  @staticmethod
  def repr(type):
    if type == Type.CLOSEP:
      return 'CLOSEP'
    if type == Type.DIV:
      return 'DIV'
    if type == Type.EOF:
      return 'EOF'
    if type == Type.FACT:
      return 'FACT'
    if type == Type.INT:
      return 'INT'
    if type == Type.MOD:
      return 'MOD'
    if type == Type.MINUS:
      return 'MINUS'
    if type == Type.MULT:
      return 'MULT'
    if type == Type.OPENP:
      return 'OPENP'
    if type == Type.PIPE:
      return 'PIPE'
    if type == Type.PLUS:
      return 'PLUS'
    if type == Type.POW:
      return 'POW'
    if type == Type.REAL:
      return 'REAL'

class Token:

  def __init__(self, type, value):
    self.type = type
    self.value = value

  def __str__(self):
    return 'Token( {type}, {value} )'.format(
      type = Type.repr(self.type),
      value = repr(self.value)
    )

  def __repr__(self):
    return self.__str__()
