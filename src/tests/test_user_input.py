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

class TestGetDecimalInput(unittest.TestCase):
    @patch('user_input.input', return_value='3.14')
    def test_get_decimal_input_valid(self, input):
        self.assertEqual(get_decimal_input(), Decimal('3.14'))

    @patch('builtins.print')
    @patch('user_input.input', side_effect=['not_decimal', '2.5'])
    @patch('user_input.sleep')
    @patch('user_input.clear_lines')
    def test_get_decimal_input_invalid(self, mock_clear_lines, mock_sleep, mock_input, mock_print):
        result = get_decimal_input()
        self.assertEqual(result, Decimal('2.5'))

        mock_sleep.assert_called_once_with(0.9)
        mock_clear_lines.assert_called_once_with(3)
        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_called_once_with("Invalid number") # I think we can ignore the error changing if it works with the default?

class TestGetPartDimension(unittest.TestCase):
    @patch('builtins.print')
    @patch('user_input.get_decimal_input', side_effect=[Decimal('10.5'), Decimal('5.25')])
    @patch('user_input.get_integer_input', return_value=4)
    @patch('user_input.get_confirmation', return_value=True)
    def test_get_part_dimension_success(self, mock_confirm, mock_int_input, mock_dec_input, mock_print):
        get_part_dimension()

        self.assertEqual(mock_dec_input.call_count, 2)
        mock_int_input.assert_called_once()
        mock_confirm.assert_called_once()
        mock_print.assert_any_call('4 parts needed of size 10.5" x 5.25", correct?\n')
        
    @patch('builtins.print')
    @patch('user_input.input', side_effect=[
        'bad',
        '8.0',
        'nope',
        '3.5',
        'wrong',
        '2',
    ])
    @patch('user_input.get_confirmation', return_value=True)
    def test_get_part_dimension_with_retries(self, mock_confirm, mock_input, mock_print):
        result = get_part_dimension()
        
        mock_confirm.assert_called_once()
        self.assertEqual(mock_input.call_count, 6)  # 3 invalid
        mock_print.assert_any_call("2 parts needed of size 8.0\" x 3.5\", correct?\n")
        self.assertIn(mock.call("Invalid number"), mock_print.call_args_list)