from src.lib.lib import Type
from src.lexer import Lexer

class Interpreter:
  
  def __init__(self, text):
    self.lexer = Lexer(text)
    self.token = self.lexer.get_next_token()
    self.ae()

  @staticmethod
  def is_first_of_term(type):
    return type == Type.UNION or type == Type.DIFF or \
        type == Type.NOT or type == Type.CARD or \
        type == Type.ID or type == Type.NULL or \
        type == Type.INT or type == Type.REAL or \
        type == Type.BOOL or type == Type.STRING or \
        type == Type.OPENP or type == Type.OPENB or \
        type == Type.OPENC
  
  def ae(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.c5e()
    else:
      raise
    if self.token.type != Type.EOF:
      raise
  
  def c5e(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.c4e()
      self.c5e_prime()
    else:
      raise
  
  def c5e_prime(self):
    if self.token.type == Type.EQ or self.token.type == Type.NEQ or \
        self.token.type == Type.GT or self.token.type == Type.GTEQ or \
        self.token.type == Type.LT or self.token.type == Type.LTEQ:
      self.c5o()
      self.c5e()
  
  def c5o(self):
    if self.token.type == Type.EQ:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.NEQ:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.GT:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.GTEQ:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.LT:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.LTEQ:
      self.token = self.lexer.get_next_token()
    else:
      raise
  
  def c4e(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.c3e()
      self.c4e_prime()
    else:
      raise
  
  def c4e_prime(self):
    if self.token.type == Type.UNION or self.token.type == Type.DIFF:
      self.c4o()
      self.c4e()
  
  def c4o(self):
    if self.token.type == Type.UNION:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.DIFF:
      self.token = self.lexer.get_next_token()
    else:
      raise
  
  def c3e(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.c2e()
      self.c3e_prime()
    else:
      raise
  
  def c3e_prime(self):
    if self.token.type == Type.AND or self.token.type == Type.XOR:
      self.c3o()
      self.c3e()
  
  def c3o(self):
    if self.token.type == Type.AND:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.XOR:
      self.token = self.lexer.get_next_token()
    else:
      raise
  
  def c2e(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.c1e()
      self.c2e_prime()
    else:
      raise
  
  def c2e_prime(self):
    if self.token.type == Type.COMPOSE or self.token.type == Type.DIV or \
        self.token.type == Type.MOD:
      self.c2o()
      self.c2e()
  
  def c2o(self):
    if self.token.type == Type.COMPOSE:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.DIV:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.MOD:
      self.token = self.lexer.get_next_token()
    else:
      raise
  
  def c1e(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.c0e()
      self.c1e_prime()
    else:
      raise
  
  def c1e_prime(self):
    if self.token.type == Type.TPOSE or self.token.type == Type.POW:
      self.c1o()
      self.c1e()
  
  def c1o(self):
    if self.token.type == Type.TPOSE:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.POW:
      self.token = self.lexer.get_next_token()
    else:
      raise
  
  def c0e(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.term()
    else:
      raise
  
  def term(self):
    if self.token.type == Type.UNION or self.token.type == Type.DIFF:
      self.unary_op()
      self.var_num_term()
    elif self.token.type == Type.NOT:
      self.token = self.lexer.get_next_token()
      if self.token.type == Type.BOOL or self.token.type == Type.NULL:
        self.bool_term()
      elif self.token.type == Type.ID:
        self.token = self.lexer.get_next_token()
      else:
        raise
    elif self.token.type == Type.ID or self.token.type == Type.INT or \
        self.token.type == Type.REAL or self.token.type == Type.CARD:
      self.var_num_term()
    elif self.token.type == Type.BOOL or self.token.type == Type.NULL or \
        self.token.type == Type.OPENP or self.token.type == type.OPENB or \
        self.token.type == Type.OPENC or self.token.type == Type.STRING:
      self.constant_term()
    else:
      raise
  
  def unary_op(self):
    if self.token.type == Type.UNION:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.DIFF:
      self.token = self.lexer.get_next_token()
    else:
      raise
  
  def var_num_term(self):
    if self.token.type == Type.ID:
      self.token = self.lexer.get_next_token()
      self.fact()
    elif self.token.type == Type.INT or self.token.type == Type.REAL or \
        self.token.type == Type.CARD:
      self.num_term()
    else:
      raise
  
  def num_term(self):
    if self.token.type == Type.INT:
      self.token = self.lexer.get_next_token()
      self.fact()
    elif self.token.type == Type.REAL:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.CARD:
      self.card_term()
      self.fact()
    else:
      raise

  def card_term(self):
    if self.token.type == Type.CARD:
      self.token = self.lexer.get_next_token()
      if self.token.type == Type.ID:
        self.token = self.lexer.get_next_token()
      elif self.token.type == Type.OPENP or self.token.type == Type.OPENB or \
          self.token.type == Type.OPENC:
        self.struct_term()
      else:
        raise
    else:
      raise
  
  def fact(self):
    if self.token.type == Type.FACT:
      self.token = self.lexer.get_next_token()
  
  def struct_term(self):
    if self.token.type == Type.OPENP:
      self.token = self.lexer.get_next_token()
      self.e_list()
      if self.token.type == Type.CLOSEP:
        self.token = self.lexer.get_next_token()
      else:
        raise
    elif self.token.type == Type.OPENB:
      self.token = self.lexer.get_next_token()
      self.e_list()
      if self.token.type == Type.CLOSEB:
        self.token = self.lexer.get_next_token()
      else:
        raise
    elif self.token.type == Type.OPENC:
      self.token = self.lexer.get_next_token()
      self.e_list()
      if self.token.type == Type.CLOSEC:
        self.token = self.lexer.get_next_token()
      else:
        raise
    else:
      raise

  def e_list(self):
    if Interpreter.is_first_of_term(self.token.type):
      self.c5e()
      self.e_list_tail()
    else:
      raise
  
  def e_list_tail(self):
    if self.token.type == Type.COMMA:
      self.token = self.lexer.get_next_token()
      self.e_list()
  
  def bool_term(self):
    if self.token.type == Type.BOOL:
      self.token = self.lexer.get_next_token()
    elif self.token.type == Type.NULL:
      self.token = self.lexer.get_next_token()
    else:
      raise
  
  def constant_term(self):
    if self.token.type == Type.BOOL or self.token.type == Type.NULL:
      self.bool_term()
    elif self.token.type == Type.OPENP or self.token.type == Type.OPENB or \
        self.token.type == Type.OPENC:
      self.struct_term()
    elif self.token.type == Type.STRING:
      self.token = self.lexer.get_next_token()
    else:
      raise
  