import random
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
        random.seed(0)

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
        self.ai_selector.focus_length_scores = [
            [0, 0, 0, 0, 0, 0] for _ in range(5)
        ]
        
        self.ai_selector.focus_length_scores[0][0] = 2
        self.ai_selector.select_best_ai()
        self.assertEqual(self.ai_selector.best_model.length, 1)
        self.assertNotEqual(self.ai_selector.best_model.length, 5)

    def test_model_choice(self):
        last_seven = ''.join(self.s1[-7:])
        model = BaseAi(1, self.trie, last_seven)

        choice = model.predict_ai_choice()
        self.assertEqual(choice, "s")
        self.assertNotEqual(choice, "k")

    def test_play_ai(self):
        self.ai_selector = AiSelector(5, self.trie)
        ai_choice = self.ai_selector.play_ai()
        self.assertEqual(ai_choice, "p")  # randomised
        self.assertNotEqual(ai_choice, "k")


class TestAiIntegration(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.sequence = ["s", "k", "k", "p", "s", "s",
                         "s", "p", "p", "s", "s", "k", "s", "s", "s"]
        self.last_seven = ""
        self.should_be_strings = [[], [("sk", 1)], [("kk", 1), ("sk", 1), ("skk", 1)], [
            ("kk", 1), ("kkp", 1), ("kp", 1), ("sk", 1), ("skk", 1), ("skkp", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kp", 1), ("kps", 1), ("ps", 1), ("sk", 1), ("skk", 1), ("skkp", 1), ("skkps", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("ps", 1), ("pss", 1), ("sk", 1), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("ss", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("ps", 1), ("pss", 1), ("psss", 1), ("sk", 1), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("ss", 2), ("sss", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("ps", 1), ("pss", 1), ("psss", 1), ("psssp", 1), ("sk", 1), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sp", 1), ("ss", 2), ("ssp", 1), ("sss", 1), ("sssp", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("kpssspp", 1), ("pp", 1), ("ps", 1), ("pss", 1), ("psss", 1), ("psssp", 1), ("pssspp", 1), ("sk", 1), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sp", 1), ("spp", 1), ("ss", 2), ("ssp", 1), ("sspp", 1), ("sss", 1), ("sssp", 1), ("ssspp", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("kpssspp", 1), ("pp", 1), ("pps", 1), ("ps", 2), ("pss", 1), ("psss", 1), ("psssp", 1), ("pssspp", 1), ("pssspps", 1), ("sk", 1), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sp", 1), ("spp", 1), ("spps", 1), ("ss", 2), ("ssp", 1), ("sspp", 1), ("sspps", 1), ("sss", 1), ("sssp", 1), ("ssspp", 1), ("ssspps", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("kpssspp", 1), ("pp", 1), ("pps", 1), ("ppss", 1), ("ps", 2), ("pss", 2), ("psss", 1), ("psssp", 1), ("pssspp", 1), ("pssspps", 1), ("sk", 1), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sp", 1), ("spp", 1), ("spps", 1), ("sppss", 1), ("ss", 3), ("ssp", 1), ("sspp", 1), ("sspps", 1), ("ssppss", 1), ("sss", 1), ("sssp", 1), ("ssspp", 1), ("ssspps", 1), ("sssppss", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("kpssspp", 1), ("pp", 1), ("pps", 1), ("ppss", 1), ("ppssk", 1), ("ps", 2), ("pss", 2), ("pssk", 1), ("psss", 1), ("psssp", 1), ("pssspp", 1), ("pssspps", 1), ("sk", 2), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sp", 1), ("spp", 1), ("spps", 1), ("sppss", 1), ("sppssk", 1), ("ss", 3), ("ssk", 1), ("ssp", 1), ("sspp", 1), ("sspps", 1), ("ssppss", 1), ("ssppssk", 1), ("sss", 1), ("sssp", 1), ("ssspp", 1), ("ssspps", 1), ("sssppss", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("kpssspp", 1), ("ks", 1), ("pp", 1), ("pps", 1), ("ppss", 1), ("ppssk", 1), ("ppssks", 1), ("ps", 2), ("pss", 2), ("pssk", 1), ("pssks", 1), ("psss", 1), ("psssp", 1), ("pssspp", 1), ("pssspps", 1), ("sk", 2), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sks", 1), ("sp", 1), ("spp", 1), ("spps", 1), ("sppss", 1), ("sppssk", 1), ("sppssks", 1), ("ss", 3), ("ssk", 1), ("ssks", 1), ("ssp", 1), ("sspp", 1), ("sspps", 1), ("ssppss", 1), ("ssppssk", 1), ("sss", 1), ("sssp", 1), ("ssspp", 1), ("ssspps", 1), ("sssppss", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("kpssspp", 1), ("ks", 1), ("kss", 1), ("pp", 1), ("pps", 1), ("ppss", 1), ("ppssk", 1), ("ppssks", 1), ("ppsskss", 1), ("ps", 2), ("pss", 2), ("pssk", 1), ("pssks", 1), ("psskss", 1), ("psss", 1), ("psssp", 1), ("pssspp", 1), ("pssspps", 1), ("sk", 2), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sks", 1), ("skss", 1), ("sp", 1), ("spp", 1), ("spps", 1), ("sppss", 1), ("sppssk", 1), ("sppssks", 1), ("ss", 4), ("ssk", 1), ("ssks", 1), ("sskss", 1), ("ssp", 1), ("sspp", 1), ("sspps", 1), ("ssppss", 1), ("ssppssk", 1), ("sss", 1), ("sssp", 1), ("ssspp", 1), ("ssspps", 1), ("sssppss", 1)], [
            ("kk", 1), ("kkp", 1), ("kkps", 1), ("kkpss", 1), ("kkpsss", 1), ("kkpsssp", 1), ("kp", 1), ("kps", 1), ("kpss", 1), ("kpsss", 1), ("kpsssp", 1), ("kpssspp", 1), ("ks", 1), ("kss", 1), ("ksss", 1), ("pp", 1), ("pps", 1), ("ppss", 1), ("ppssk", 1), ("ppssks", 1), ("ppsskss", 1), ("ps", 2), ("pss", 2), ("pssk", 1), ("pssks", 1), ("psskss", 1), ("pssksss", 1), ("psss", 1), ("psssp", 1), ("pssspp", 1), ("pssspps", 1), ("sk", 2), ("skk", 1), ("skkp", 1), ("skkps", 1), ("skkpss", 1), ("skkpsss", 1), ("sks", 1), ("skss", 1), ("sksss", 1), ("sp", 1), ("spp", 1), ("spps", 1), ("sppss", 1), ("sppssk", 1), ("sppssks", 1), ("ss", 5), ("ssk", 1), ("ssks", 1), ("sskss", 1), ("ssksss", 1), ("ssp", 1), ("sspp", 1), ("sspps", 1), ("ssppss", 1), ("ssppssk", 1), ("sss", 2), ("sssp", 1), ("ssspp", 1), ("ssspps", 1), ("sssppss", 1)]]

    def test_trie_15_rounds(self):
        for i in range(len(self.sequence)):
            if len(self.last_seven) < 7:
                self.last_seven += self.sequence[i]
            else:
                self.last_seven = self.last_seven[1:] + self.sequence[i]

            if len(self.last_seven) >= 2:
                for length in range(2, len(self.last_seven) + 1):
                    substring = self.last_seven[-length:]
                    self.trie.add(substring)

            all_strings_with_frequencies = self.trie.get_all_strings_with_frequencies()
            self.assertEqual(all_strings_with_frequencies,
                             self.should_be_strings[i])
