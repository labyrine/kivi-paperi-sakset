import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_add_and_get_next_frequencies(self):
        self.trie.add("kp")
        self.assertEqual(self.trie.get_next_frequencies("k"), {'p': 1})
        self.trie.add("kps")
        self.assertEqual(self.trie.get_next_frequencies("kp"), {'s': 1})
        self.trie.add("ks")
        self.assertEqual(self.trie.get_next_frequencies("k"), {'p': 1, 's': 1})
