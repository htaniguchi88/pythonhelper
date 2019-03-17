import unittest
import interleave


class TestInterleave(unittest.TestCase):

  def test_interleave_all_characters(self):
    input = ['aa', 'bb', 'cc']
    self.assertEqual('abcabc', interleave.interleave_all_characters(input))
