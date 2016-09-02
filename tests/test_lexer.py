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
    self.assertEqual(lexer.get_next_token(), Token(Type.DOT, '*'))
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
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  
  def test_integer_subtraction(self):
    lexer = Lexer('1 - 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.MINUS, '-'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_parenthesis(self):
    lexer = Lexer('( 1 )')
    self.assertEqual(lexer.get_next_token(), Token(Type.OPENP, '('))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.CLOSEP, ')'))
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
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 2.5))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_integer_no_leading_zeros(self):
    lexer = Lexer('0 + 00')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_real_no_leading_zeros(self):
    lexer = Lexer('0.00 + 00.0')
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 0.00))
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 0))
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 0.0))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))

  def test_real_must_have_fraction(self):
    lexer = Lexer('0.0 + 0.')
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 0.0))
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertRaises(Exception, lexer.get_next_token)

  def test_real_must_have_fraction_again(self):
    lexer = Lexer('1.0 + 1.')
    self.assertEqual(lexer.get_next_token(), Token(Type.REAL, 1.0))
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertRaises(Exception, lexer.get_next_token)

  def test_no_unknown_symbols(self):
    lexer = Lexer('1 + @')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertRaises(Exception, lexer.get_next_token)
  
  def test_ignore_comments(self):
    lexer = Lexer('# comment \n 1 + 1')
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.PLUS, '+'))
    self.assertEqual(lexer.get_next_token(), Token(Type.INT, 1))
    self.assertEqual(lexer.get_next_token(), Token(Type.EOF, ''))
  