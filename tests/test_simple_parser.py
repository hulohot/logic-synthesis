import unittest
import sys
from logic_synthesis.parser import parser
from logic_synthesis.lexer import lexer

class TestLexer(unittest.TestCase):

    def test_tokens(self):
        data = "3 + 4 * 10 + -20 * 2;"
        expected_tokens = [
            ('NUMBER', 3),
            ('PLUS', '+'),
            ('NUMBER', 4),
            ('TIMES', '*'),
            ('NUMBER', 10),
            ('PLUS', '+'),
            ('MINUS', '-'),
            ('NUMBER', 20),
            ('TIMES', '*'),
            ('NUMBER', 2),
            ('SEMICOLON', ';')
        ]

        lexer.input(data)  # Feed data to the lexer

        for i, (tok_type, tok_val) in enumerate(expected_tokens):
            tok = lexer.token()
            self.assertIsNotNone(tok, f"Token at index {i} should not be None")
            self.assertEqual(tok.type, tok_type, f"Token type mismatch at index {i}")
            self.assertEqual(tok.value, tok_val, f"Token value mismatch at index {i}")

        # Ensure no more tokens are left
        self.assertIsNone(lexer.token(), "There should be no more tokens left after processing")

class TestParser(unittest.TestCase):

    def test_simple_expression(self):
        data = "3 + 4 * 10 + -20 * 2;"
        result = parser.parse(data, lexer=lexer)
        expected_result = 3 + (4 * 10) + (-20 * 2)
        self.assertIsNotNone(result, "Parser returned None, expected an expression result")
        self.assertEqual(result, expected_result, "Parsed expression does not match expected result")


if __name__ == '__main__':
    unittest.main()
