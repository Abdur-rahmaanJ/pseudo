import unittest
import math
from src.lexer import Lexer
from src.lib.lib import Token, Type

class TestLexer(unittest.TestCase):

  def test_integer_fact(self):
    lexer = Lexer('1!')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.FACT, '!'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_pow(self):
    lexer = Lexer('1 ** 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.POW, '**'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_composition(self):
    lexer = Lexer('1 * 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.COMPOSE, '*'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_division(self):
    lexer = Lexer('1 / 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.DIV, '/'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_modulus(self):
    lexer = Lexer('1 % 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.MOD, '%'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_union(self):
    lexer = Lexer('1 + 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_integer_difference(self):
    lexer = Lexer('1 - 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.DIFF, '-'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_absolute_value(self):
    lexer = Lexer('| 1 |')
    self.assertEqual(lexer.get_next_token(), Token(Type.PIPE, '|'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.PIPE, '|'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_real_union(self):
    lexer = Lexer('3.0 + 2.5')
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 3.0))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 2.5))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_no_leading_zeros(self):
    lexer = Lexer('0 + 00')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_real_no_leading_zeros(self):
    lexer = Lexer('0.00 + 00.0')
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 0.00))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 0.0))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_real_must_have_fraction(self):
    lexer = Lexer('0.0 + 0.')
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 0.0))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertRaises(Exception, lexer.get_next_token)

  def test_real_must_have_fraction_again(self):
    lexer = Lexer('1.0 + 1.')
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 1.0))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertRaises(Exception, lexer.get_next_token)

  def test_no_unknown_symbols(self):
    lexer = Lexer('1 + @')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertRaises(Exception, lexer.get_next_token)
  
  def test_ignore_single_line_comment(self):
    lexer = Lexer('// comment \n 1 + 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_ignore_multi_line_comment(self):
    lexer = Lexer('/* comment \n\n\n\n */ \n 1 + 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_multi_line_comment_must_close(self):
    lexer = Lexer('/* comment \n\n\n\n')
    self.assertRaises(Exception, lexer.get_next_token)

  def test_double_quoted_string(self):
    lexer = Lexer('"#HelloWorld123"')
    self.assertEqual(lexer.get_next_token(), Token(Type.STRING, '#HelloWorld123'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_double_quoted_string_must_close(self):
    lexer = Lexer('"#HelloWorld123')
    self.assertRaises(Exception, lexer.get_next_token)

  def test_single_quoted_string(self):
    lexer = Lexer("'#HelloWorld123'")
    self.assertEqual(lexer.get_next_token(), Token(Type.STRING, '#HelloWorld123'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_single_quoted_string_must_close(self):
    lexer = Lexer('"#HelloWorld123')
    self.assertRaises(Exception, lexer.get_next_token)

  def test_id(self):
    lexer = Lexer('abc``')
    self.assertEqual(lexer.get_next_token(), Token(Type.ID, 'abc``'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_id_with_underscore(self):
    lexer = Lexer('abc``_t``')
    self.assertEqual(lexer.get_next_token(), Token(Type.ID, 'abc``'))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNDER, '_'))
    self.assertEqual(lexer.get_next_token(), Token(Type.ID, 't``'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_tuple_union(self):
    lexer = Lexer('(1) + (1)')
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENP, '('))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEP, ')'))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENP, '('))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEP, ')'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_list_union(self):
    lexer = Lexer('[1] + [1]')
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENB, '['))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEB, ']'))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENB, '['))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEB, ']'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_set_union(self):
    lexer = Lexer('{1} + {1}')
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENC, '{'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEC, '}'))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENC, '{'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEC, '}'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_set_and(self):
    lexer = Lexer('{1} & {1}')
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENC, '{'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEC, '}'))
    self.assertEqual(lexer.get_next_token(), Token(Type.AND, '&'))
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENC, '{'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEC, '}'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_set_xor(self):
    lexer = Lexer('{1} ^ {1}')
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENC, '{'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEC, '}'))
    self.assertEqual(lexer.get_next_token(), Token(Type.XOR, '^'))
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENC, '{'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEC, '}'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_reserved_words(self):
    lexer = Lexer('else forall if in is let of st then while')
    self.assertEqual(lexer.get_next_token(), Token(Type.ELSE, 'else'))
    self.assertEqual(lexer.get_next_token(), Token(Type.FORALL, 'forall'))
    self.assertEqual(lexer.get_next_token(), Token(Type.IF, 'if'))
    self.assertEqual(lexer.get_next_token(), Token(Type.IN, 'in'))
    self.assertEqual(lexer.get_next_token(), Token(Type.IS, 'is'))
    self.assertEqual(lexer.get_next_token(), Token(Type.LET, 'let'))
    self.assertEqual(lexer.get_next_token(), Token(Type.OF, 'of'))
    self.assertEqual(lexer.get_next_token(), Token(Type.ST, 'st'))
    self.assertEqual(lexer.get_next_token(), Token(Type.THEN, 'then'))
    self.assertEqual(lexer.get_next_token(), Token(Type.WHILE, 'while'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_reserved_values(self):
    lexer = Lexer('e false null pi true')
    self.assertEqual(lexer.get_next_token(), Token(Type.E, math.e))
    self.assertEqual(lexer.get_next_token(), Token(Type.BOOL, False))
    self.assertEqual(lexer.get_next_token(), Token(Type.NULL, None))
    self.assertEqual(lexer.get_next_token(), Token(Type.PI, math.pi))
    self.assertEqual(lexer.get_next_token(), Token(Type.BOOL, True))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_reserved_operators(self):
    lexer = Lexer('and diff iff inter mod not onlyif or to xor union')
    self.assertEqual(lexer.get_next_token(), Token(Type.AND, '&'))
    self.assertEqual(lexer.get_next_token(), Token(Type.DIFF, '-'))
    self.assertEqual(lexer.get_next_token(), Token(Type.IFF, '<=>'))
    self.assertEqual(lexer.get_next_token(), Token(Type.AND, '&'))
    self.assertEqual(lexer.get_next_token(), Token(Type.MOD, '%'))
    self.assertEqual(lexer.get_next_token(), Token(Type.NOT, '~'))
    self.assertEqual(lexer.get_next_token(), Token(Type.IMPL, '=>'))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.TO, '->'))
    self.assertEqual(lexer.get_next_token(), Token(Type.XOR, '^'))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_reserved_types(self):
    lexer = Lexer('B Boolean Integer N Natural Q Rational R Real S String U Universal Z')
    self.assertEqual(lexer.get_next_token(), Token(Type.B, 'B'))
    self.assertEqual(lexer.get_next_token(), Token(Type.B, 'B'))
    self.assertEqual(lexer.get_next_token(), Token(Type.Z, 'Z'))
    self.assertEqual(lexer.get_next_token(), Token(Type.N, 'N'))
    self.assertEqual(lexer.get_next_token(), Token(Type.N, 'N'))
    self.assertEqual(lexer.get_next_token(), Token(Type.Q, 'Q'))
    self.assertEqual(lexer.get_next_token(), Token(Type.Q, 'Q'))
    self.assertEqual(lexer.get_next_token(), Token(Type.R, 'R'))
    self.assertEqual(lexer.get_next_token(), Token(Type.R, 'R'))
    self.assertEqual(lexer.get_next_token(), Token(Type.S, 'S'))
    self.assertEqual(lexer.get_next_token(), Token(Type.S, 'S'))
    self.assertEqual(lexer.get_next_token(), Token(Type.U, 'U'))
    self.assertEqual(lexer.get_next_token(), Token(Type.U, 'U'))
    self.assertEqual(lexer.get_next_token(), Token(Type.Z, 'Z'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  