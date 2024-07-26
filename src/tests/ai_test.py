import unittest
from ai import BaseAi


class MockTrie:
    def __init__(self, frequencies):
        self.frequencies = frequencies

    def get_next_frequencies(self, substring):
        return self.frequencies.get(substring, {})


class TestBaseAi(unittest.TestCase):
    def setUp(self):
        self.length = 3
        self.last_seven1 = "kpskpsk"
        self.frequencies = {"psk": {"k": 1, "p": 2, "s": 3}}
        self.trie_mock = MockTrie(self.frequencies)

    def test_prediction(self):
        ai = BaseAi(self.length, self.trie_mock, self.last_seven1)
        self.assertEqual(ai.prediction(), "k")

    def test_counter_move(self):
        ai = BaseAi(self.length, self.trie_mock, self.last_seven1)
        self.assertEqual(ai.counter_move("k"), "p")
        self.assertEqual(ai.counter_move("p"), "s")
        self.assertEqual(ai.counter_move("s"), "k")
