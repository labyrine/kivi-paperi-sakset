import unittest

from ai import BaseAi, AiSelector
from trie import Trie


class TestIntegration(unittest.TestCase):
    def setUp(self):

        self.trie = Trie()
        self.s1 = "kpskpsk"
        s2 = "kpskps"
        s3 = "kpskp"
        s4 = "kpsk"
        s5 = "kps"
        s6 = "kp"

        for length in range(2, len(self.s1) + 1):
            substring = self.s1[-length:]
            self.trie.add(substring)
        for length in range(2, len(s2) + 1):
            substring = s2[-length:]
            self.trie.add(substring)
        for length in range(2, len(s3) + 1):
            substring = s3[-length:]
            self.trie.add(substring)
        for length in range(2, len(s4) + 1):
            substring = s4[-length:]
            self.trie.add(substring)
        for length in range(2, len(s5) + 1):
            substring = s5[-length:]
            self.trie.add(substring)
        for length in range(2, len(s6) + 1):
            substring = s6[-length:]
            self.trie.add(substring)
        self.ai_selector = AiSelector(5, self.trie)

    def test_trie_structure(self):
        all_strings_with_frequencies = self.trie.get_all_strings_with_frequencies()
        should_be_strings = [
            ("kp", 2),
            ("kps", 2),
            ("kpsk", 2),
            ("kpskp", 1),
            ("kpskps", 1),
            ("kpskpsk", 1),
            ("ps", 2),
            ("psk", 2),
            ("pskp", 1),
            ("pskps", 1),
            ("pskpsk", 1),
            ("sk", 2),
            ("skp", 1),
            ("skps", 1),
            ("skpsk", 1)
        ]
        self.assertEqual(all_strings_with_frequencies, should_be_strings)
        self.assertNotEqual(all_strings_with_frequencies, "")

    def test_model_selection_and_choice(self):

        self.ai_selector = AiSelector(5, self.trie)
        selected_model = self.ai_selector.select_best_ai()
        self.assertEqual(selected_model.length, 1)
        self.assertNotEqual(selected_model.length, 5)

    def test_model_choice(self):
        last_seven = ''.join(self.s1[-7:])
        model = BaseAi(1, self.trie, last_seven)

        choice = model.prediction()
        self.assertEqual(choice, "s")
        self.assertNotEqual(choice, "k")
