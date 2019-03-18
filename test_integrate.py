import unittest
import integrate


class TestIntegrate(unittest.TestCase):

    def test_integrate_words_same_characters_length_and_two_words(self):
        input = ['a', 'b']
        self.assertEqual('ab', integrate.integrate_words(input))

    def test_integrate_words_same_characters_length_and_three_words(self):
        input = ['a', 'b', 'c']
        self.assertEqual('abc', integrate.integrate_words(input))

    def test_integrate_words_deferent_characters_length_and_three_words(self):
        input = ['a', 'bb', 'ccc']
        self.assertEqual('abbccc', integrate.integrate_words(input))
