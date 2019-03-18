import unittest
import interleave


class TestInterleave(unittest.TestCase):

    def test_interleave_same_characters_length_and_three_words(self):
        input = ['aa', 'bb', 'cc']
        self.assertEqual('abcabc', interleave.interleave_all_characters(input))

    def test_interleave_deferent_characters_length_and_three_words(self):
        input = ['a', 'bb', 'ccc']
        self.assertEqual('abcbcc', interleave.interleave_all_characters(input))

    def test_interleave_one_character_and_one_word(self):
        input = ['a']
        self.assertEqual('a', interleave.interleave_all_characters(input))

    def test_interleave_deferent_characters_length_and_two_words(self):
        input = ['a', 'bb']
        self.assertEqual('abb', interleave.interleave_all_characters(input))
