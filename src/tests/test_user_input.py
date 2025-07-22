import unittest
from unittest import mock
from unittest.mock import patch

from user_input import *

class TestGetConfirmation(unittest.TestCase):
    @patch('user_input.input', return_value='y')
    def test_get_confirmation_yes(self, input):
        self.assertTrue(get_confirmation())

    @patch('user_input.input', return_value='n')
    def test_get_confirmation_no(self, input):
        self.assertFalse(get_confirmation())

    # Decorators:
    @patch('builtins.print')
    @patch('user_input.clear_lines')
    @patch('user_input.sleep')
    @patch('user_input.input', side_effect=['invalid','y'])
    def test_get_confirmation_invalid(self, mock_input, mock_sleep, mock_clear_lines, mock_print):
        # Decorators are applied applied bottom to top, so the last one is the first to be executed
        # Notice that we then apply the mocks in the function input top to bottom
        result = get_confirmation()
        self.assertTrue(result)  # Should return True after valid input

        mock_input.assert_called_with("Y or N?\n")
        self.assertEqual(mock_input.call_count, 2)  # Called twice: once for invalid, once for valid
        mock_sleep.assert_called_once_with(0.5)
        mock_clear_lines.assert_called_once_with(3)
        mock_print.assert_called_once_with("Invalid input")

class TestIsDecimal(unittest.TestCase):
    def test_is_decimal_valid(self):
        self.assertTrue(is_decimal('3.14'))
        self.assertTrue(is_decimal('0.001'))
        self.assertTrue(is_decimal('-2.5'))

    def test_is_decimal_invalid(self):
        self.assertFalse(is_decimal('not decimal'))
        self.assertFalse(is_decimal('12,34'))  # Comma instead of dot
        self.assertFalse(is_decimal(''))

class TestGetIntegerInput(unittest.TestCase):
    @patch('user_input.input', return_value='4')
    def test_get_integer_input_valid_even(self, input):
        self.assertEqual(get_integer_input(), 4)

    @patch('user_input.input', return_value='5')
    def test_get_integer_input_valid_odd(self, input):
        self.assertEqual(get_integer_input(), 5)

    @patch('user_input.input', side_effect=['not_int', '6'])
    @patch('user_input.sleep')
    @patch('user_input.clear_lines')
    def test_get_integer_input_invalid(self, mock_clear_lines, mock_sleep, mock_input):
        result = get_integer_input()
        self.assertEqual(result, 6)
        mock_sleep.assert_called_once_with(1.5)
        mock_clear_lines.assert_called_once_with(7)
        self.assertEqual(mock_input.call_count, 2)
