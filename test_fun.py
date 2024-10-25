import unittest
from unittest.mock import patch
from fun import dog_years, fizzbuzz, word_lengths, cube_sum
import sys
from io import StringIO

class TestFun(unittest.TestCase):
    @patch('builtins.input', side_effect=[20])
    def test_dog_years(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        dog_years()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "The dog's age in dog's years is 93")

    # Test fizzbuzz function
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz")
        self.assertEqual(fizzbuzz(3), "1 2 Fizz")
        self.assertEqual(fizzbuzz(5), "1 2 Fizz 4 Buzz")


    # Test word_lengths function
    def test_word_lengths(self):
        self.assertEqual(word_lengths("ChatGPT is amazing"), {'ChatGPT': 7, 'is': 2, 'amazing': 7})
        self.assertEqual(word_lengths("Hello world"), {'Hello': 5, 'world': 5})
        self.assertEqual(word_lengths("Unit testing is fun"), {'Unit': 4, 'testing': 7, 'is': 2, 'fun': 3})
        with self.assertRaises(ValueError):
            word_lengths(123)

    def test_cube_sum(self):
        self.assertEqual(cube_sum(123), 36)  # 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
        self.assertEqual(cube_sum(0), 0)  # 0^3 = 0
        self.assertEqual(cube_sum(456), 405)  # 4^3 + 5^3 + 6^3 = 64 + 125 + 216 = 405
        self.assertEqual(cube_sum(999), 2187)  # 9^3 + 9^3 + 9^3 = 729 + 729 + 729 = 2187
        with self.assertRaises(ValueError):
            cube_sum(-123)

if __name__ == "__main__":
    unittest.main()


