import unittest
import reverse


class TestReverse(unittest.TestCase):

    def test_reverse_two_characters(self):
        input = 'ab'
        self.assertEqual('ba', reverse.reverse_all_characters(input))

    def test_reverse_three_characters(self):
        input = 'abc'
        self.assertEqual('cba', reverse.reverse_all_characters(input))
