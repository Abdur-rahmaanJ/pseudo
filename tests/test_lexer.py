import unittest
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

  def test_integer_multiplication(self):
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

  def test_integer_addition(self):
    lexer = Lexer('1 + 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_integer_subtraction(self):
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

  def test_real_addition(self):
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
  
  def test_ignore_comments(self):
    lexer = Lexer('# comment \n 1 + 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

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

  def test_tuple_addition(self):
    lexer = Lexer('(1) + (1)')
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENP, '('))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEP, ')'))
    self.assertEqual(lexer.get_next_token(), Token(Type.UNION, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENP, '('))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEP, ')'))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_list_concatenation(self):
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
  
  def test_set_intersection(self):
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
    lexer = Lexer('let of if then else while forall in pi true false null mod and or not xor union inter diff given st')
    self.assertEqual(lexer.get_next_token(), Token(Type.LET, 'let'))
  