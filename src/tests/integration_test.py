import unittest

from ai import AiSelector
from trie import Trie

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
        self.should_be_best_ai = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        self.should_be_choices = ["", "", "p", "", "p", "", "k", "", "", "k", "k", "p", "k", "k", "k"]
        self.actual_choices = []

    def test_trie_15_rounds(self):
        ai_selector = AiSelector(5, self.trie)

        for i in range(len(self.sequence)):
            if len(self.last_seven) < 7:
                self.last_seven += self.sequence[i]
            else:
                self.last_seven = self.last_seven[1:] + self.sequence[i]

            ai_selector.update_last_seven(self.last_seven)

            if len(self.last_seven) >= 2:
                for length in range(2, len(self.last_seven) + 1):
                    substring = self.last_seven[-length:]
                    self.trie.add(substring)

            all_strings_with_frequencies = self.trie.get_all_strings_with_frequencies()
            self.assertEqual(all_strings_with_frequencies,
                             self.should_be_strings[i])
            
            ai_selector.update_scores()
            ai_selector.select_best_ai()

            self.assertEqual(ai_selector.best_model.length, self.should_be_best_ai[i])

            prediction = ai_selector.best_model.predict_ai_choice()
            self.actual_choices.append(prediction)
        
        self.assertEqual(self.should_be_choices, self.actual_choices)

