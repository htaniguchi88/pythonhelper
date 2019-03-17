import unittest
import interleave


class TestInterleave(unittest.TestCase):

  def test_interleave_all_characters(self):
    input = ['aa', 'bb', 'cc']
    self.assertEqual(['a', 'b', 'c', 'a', 'b', 'c'], interleave.interleave_all_characters(input))
