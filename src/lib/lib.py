class Type:
  AND, \
  ARRAY, \
  B, \
  BOOL, \
  CARD, \
  CLOSEB, \
  CLOSEC, \
  CLOSEP, \
  COLON, \
  COMMA, \
  COMPOSE, \
  DF, \
  DEFAS, \
  DICT, \
  DIFF, \
  DIV, \
  DOM, \
  ELSE, \
  EOF, \
  EQ, \
  FACT, \
  FORALL, \
  FUN, \
  GT, \
  GTEQ, \
  ID, \
  IF, \
  IN, \
  IS, \
  INT, \
  INTERVAL, \
  LET, \
  LT, \
  LTEQ, \
  MAP, \
  MATRIX, \
  MOD, \
  N, \
  NEQ, \
  NORM, \
  NOT, \
  NULL, \
  OF, \
  OPENB, \
  OPENC, \
  OPENP, \
  PERIOD, \
  PI, \
  PIPE, \
  POW, \
  Q, \
  QUEST, \
  R, \
  RANGE, \
  REAL, \
  S, \
  SEMIC, \
  SEQ, \
  SET, \
  ST, \
  STRING, \
  THEN, \
  TO, \
  TPOSE, \
  TUPLE, \
  U, \
  UNDER, \
  UNION, \
  VEC, \
  WHILE, \
  XOR, \
  Z = range(72)

  @staticmethod
  def repr(type):
    if type == Type.AND:
      return 'AND'
    if type == Type.ARRAY:
      return 'ARRAY'
    if type == Type.B:
      return 'B'
    if type == Type.BOOL:
      return 'BOOL'
    if type == Type.CARD:
      return 'CARD'
    if type == Type.CLOSEB:
      return 'CLOSEB'
    if type == Type.CLOSEC:
      return 'CLOSEC'
    if type == Type.CLOSEP:
      return 'CLOSEP'
    if type == Type.COLON:
      return 'COLON'
    if type == Type.COMMA:
      return 'COMMA'
    if type == Type.COMPOSE:
      return 'COMPOSE'
    if type == Type.DF:
      return 'DF'
    if type == Type.DEFAS:
      return 'DEFAS'
    if type == Type.DICT:
      return 'DICT'
    if type == Type.DIFF:
      return 'DIFF'
    if type == Type.DIV:
      return 'DIV'
    if type == Type.DOM:
      return 'DOM'
    if type == Type.ELSE:
      return 'ELSE'
    if type == Type.EOF:
      return 'EOF'
    if type == Type.EQ:
      return 'EQ'
    if type == Type.FACT:
      return 'FACT'
    if type == Type.FORALL:
      return 'FORALL'
    if type == Type.FUN:
      return 'FUN'
    if type == Type.GT:
      return 'GT'
    if type == Type.GTEQ:
      return 'GTEQ'
    if type == Type.ID:
      return 'ID'
    if type == Type.IF:
      return 'IF'
    if type == Type.IN:
      return 'IN'
    if type == Type.IS:
      return 'IN'
    if type == Type.INT:
      return 'INT'
    if type == Type.INTERVAL:
      return 'INTERVAL'
    if type == Type.LET:
      return 'LET'
    if type == Type.LT:
      return 'LT'
    if type == Type.LTEQ:
      return 'LTEQ'
    if type == Type.MAP:
      return 'MAP'
    if type == Type.MATRIX:
      return 'MATRIX'
    if type == Type.MOD:
      return 'MOD'
    if type == Type.N:
      return 'N'
    if type == Type.NEQ:
      return 'NEQ'
    if type == Type.NORM:
      return 'NORM'
    if type == Type.NOT:
      return 'NOT'
    if type == Type.NULL:
      return 'NULL'
    if type == Type.OF:
      return 'OF'
    if type == Type.OPENB:
      return 'OPENB'
    if type == Type.OPENC:
      return 'OPENC'
    if type == Type.OPENP:
      return 'OPENP'
    if type == Type.PERIOD:
      return 'PERIOD'
    if type == Type.PI:
      return 'PI'
    if type == Type.PIPE:
      return 'PIPE'
    if type == Type.POW:
      return 'POW'
    if type == Type.Q:
      return 'Q'
    if type == Type.QUEST:
      return 'QUEST'
    if type == Type.R:
      return 'R'
    if type == Type.RANGE:
      return 'RANGE'
    if type == Type.REAL:
      return 'REAL'
    if type == Type.S:
      return 'S'
    if type == Type.SEMIC:
      return 'SEMIC'
    if type == Type.SEQ:
      return 'SEQ'
    if type == Type.SET:
      return 'SET'
    if type == Type.ST:
      return 'ST'
    if type == Type.STRING:
      return 'STRING'
    if type == Type.THEN:
      return 'THEN'
    if type == Type.TO:
      return 'TO'
    if type == Type.TPOSE:
      return 'TPOSE'
    if type == Type.TUPLE:
      return 'TUPLE'
    if type == Type.U:
      return 'U'
    if type == Type.UNDER:
      return 'UNDER'
    if type == Type.UNION:
      return 'UNION'
    if type == Type.VEC:
      return 'VEC'
    if type == Type.WHILE:
      return 'WHILE'
    if type == Type.XOR:
      return 'XOR'
    if type == Type.Z:
      return 'Z'

class Token:

  def __init__(self, type, value):
    self.type = type
    self.value = value

  def __eq__(self, token):
    return self.type == token.type and self.value == token.value

  def __str__(self):
    return 'Token( {type}, {value} )'.format(
      type = Type.repr(self.type),
      value = repr(self.value)
    )

  def __repr__(self):
    return self.__str__()

class Reserved:

    def __init__(self):
      self.words = {
        'and': Token(Type.AND, '&'),
        'B': Token(Type.B, 'B'),
        'Boolean': Token(Type.B, 'B'),
        'else': Token(Type.ELSE, 'else'),
        'false': Token(Type.BOOL, False),
        'forall': Token(Type.FORALL, 'forall'),
        'if': Token(Type.IF, 'if'),
        'in': Token(Type.IN, 'in'),
        'is': Token(Type.IS, 'is'),
        'Integer': Token(Type.Z, 'Z'),
        'let': Token(Type.LET, 'let'),
        'mod': Token(Type.MOD, '%'),
        'N': Token(Type.N, 'N'),
        'Natural': Token(Type.N, 'N'),
        'null': Token(Type.NULL, 'null'),
        'of': Token(Type.OF, 'of'),
        'pi': Token(Type.PI, 'pi'),
        'Q': Token(Type.Q, 'Q'),
        'Rational': Token(Type.Q, 'Q'),
        'R': Token(Type.R, 'R'),
        'Real': Token(Type.R, 'R'),
        'S': Token(Type.S, 'S'),
        'st': Token(Type.ST, 'st'),
        'String': Token(Type.S, 'S'),
        'then': Token(Type.THEN, 'then'),
        'to': Token(Type.TO, '->'),
        'true': Token(Type.BOOL, True),
        'U': Token(Type.U, 'U'),
        'Universal': Token(Type.U, 'U'),
        'while': Token(Type.WHILE, 'while'),
        'xor': Token(Type.XOR, '^'),
        'Z': Token(Type.Z, 'Z')
      }
