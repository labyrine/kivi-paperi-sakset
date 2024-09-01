import unittest
from game_components import ScoreManager, LastSevenManager


class MockTrie:
    def __init__(self):
        self.frequencies = {}
        self.added_substrings = []

    def add(self, substring):
        self.added_substrings.append(substring)


class TestScoreManager(unittest.TestCase):
    def setUp(self):
        self.score_manager = ScoreManager()

    def test_draw(self):
        result = self.score_manager.who_won("k", "k")
        self.assertEqual(result, "Tasapeli")
        self.assertEqual(self.score_manager.draw, 1)
        self.assertEqual(self.score_manager.player_points, 0)
        self.assertEqual(self.score_manager.ai_points, 0)

    def test_player_won(self):
        result1 = self.score_manager.who_won("k", "s")
        self.assertEqual(result1, "Sinä voitit")
        self.assertEqual(self.score_manager.draw, 0)
        self.assertEqual(self.score_manager.player_points, 1)
        self.assertEqual(self.score_manager.ai_points, 0)

        result2 = self.score_manager.who_won("s", "p")
        self.assertEqual(result2, "Sinä voitit")
        self.assertEqual(self.score_manager.draw, 0)
        self.assertEqual(self.score_manager.player_points, 2)
        self.assertEqual(self.score_manager.ai_points, 0)

        result3 = self.score_manager.who_won("p", "k")
        self.assertEqual(result3, "Sinä voitit")
        self.assertEqual(self.score_manager.draw, 0)
        self.assertEqual(self.score_manager.player_points, 3)
        self.assertEqual(self.score_manager.ai_points, 0)

    def test_player_lost(self):
        result1 = self.score_manager.who_won("s", "k")
        self.assertEqual(result1, "Pelikone voitti")
        self.assertEqual(self.score_manager.draw, 0)
        self.assertEqual(self.score_manager.player_points, 0)
        self.assertEqual(self.score_manager.ai_points, 1)

        result2 = self.score_manager.who_won("p", "s")
        self.assertEqual(result2, "Pelikone voitti")
        self.assertEqual(self.score_manager.draw, 0)
        self.assertEqual(self.score_manager.player_points, 0)
        self.assertEqual(self.score_manager.ai_points, 2)

        result3 = self.score_manager.who_won("k", "p")
        self.assertEqual(result3, "Pelikone voitti")
        self.assertEqual(self.score_manager.draw, 0)
        self.assertEqual(self.score_manager.player_points, 0)
        self.assertEqual(self.score_manager.ai_points, 3)


class TestLastSevenManager(unittest.TestCase):
    def setUp(self):
        self.trie_mock = MockTrie()
        self.last_seven_manager = LastSevenManager(self.trie_mock)

    def test_update_string_when_string_short(self):
        self.last_seven_manager.update_string("k")
        self.assertEqual(self.last_seven_manager.last_seven, "k")

    def test_update_string_when_string_long(self):
        for c in "kpskpskp":
            self.last_seven_manager.update_string(c)
        self.assertEqual(self.last_seven_manager.last_seven, "pskpskp")

    def test_save_player_choice_to_trie_when_last_seven_long(self):
        for c in "kpskpsk":
            self.last_seven_manager.update_string(c)

        self.last_seven_manager.save_player_choice_to_trie()
        expected_substrings = ["sk", "psk",
                               "kpsk", "skpsk", "pskpsk", "kpskpsk"]
        self.assertEqual(self.trie_mock.added_substrings, expected_substrings)

    def test_save_player_choice_to_trie_when_last_seven_short(self):
        self.last_seven_manager.update_string("k")
        self.last_seven_manager.save_player_choice_to_trie()
        self.assertEqual(self.trie_mock.added_substrings, [])
