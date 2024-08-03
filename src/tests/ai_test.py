import unittest
from unittest.mock import patch, MagicMock
from ai import BaseAi, AiSelector


class MockTrie:
    def __init__(self, frequencies):
        self.frequencies = frequencies

    def get_next_frequencies(self, substring):
        return self.frequencies.get(substring, {})


class TestBaseAi(unittest.TestCase):
    def setUp(self):
        self.length = 3
        self.last_seven1 = "kpskpsk"
        self.last_seven2 = "kp"
        self.frequencies = {"psk": {"k": 1, "p": 2, "s": 3}}
        self.trie_mock = MockTrie(self.frequencies)

    def test_prediction_kps(self):
        ai = BaseAi(self.length, self.trie_mock, self.last_seven1)
        self.assertEqual(ai.prediction(), "k")

    def test_prediction_short(self):
        ai = BaseAi(self.length, self.trie_mock, self.last_seven2)
        self.assertEqual(ai.prediction(), "")

    def test_prediction_empty(self):
        ai = BaseAi(2, self.trie_mock, self.last_seven1)
        self.assertEqual(ai.prediction(), "")

    def test_counter_move(self):
        ai = BaseAi(self.length, self.trie_mock, self.last_seven1)
        self.assertEqual(ai.counter_move("k"), "p")
        self.assertEqual(ai.counter_move("p"), "s")
        self.assertEqual(ai.counter_move("s"), "k")


class TestAiSelector(unittest.TestCase):
    def setUp(self):
        self.length = 3
        self.last_seven1 = "kpskpsk"
        self.frequencies = {"psk": {"k": 1, "p": 2, "s": 3}}
        self.trie_mock = MockTrie(self.frequencies)

    @patch('ai.BaseAi')
    def test_update_last_seven(self, MockBaseAi):
        mock_base_ai_instance = MagicMock()
        MockBaseAi.side_effect = [mock_base_ai_instance for _ in range(6)]

        ai_selector = AiSelector(5, self.trie_mock)
        ai_selector.update_last_seven(self.last_seven1)

        for model in ai_selector.models:
            self.assertEqual(model.last_seven, self.last_seven1)

    @patch('ai.BaseAi')
    def test_update_scores_p(self, MockBaseAi):
        mock_base_ai_instance = MagicMock()
        mock_base_ai_instance.prediction.side_effect = [
            "k", "p", "s", "k", "p", "s"]
        MockBaseAi.side_effect = [mock_base_ai_instance for _ in range(6)]

        ai_selector = AiSelector(5, self.trie_mock)
        ai_selector.update_scores("p")

        valid_scores_p = [-1, 0, 1, -1, 0, 1]
        valid_stats_p = [
            {"tasapelit": 0, "voitot": 0, "häviöt": 1},
            {"tasapelit": 1, "voitot": 0, "häviöt": 0},
            {"tasapelit": 0, "voitot": 1, "häviöt": 0},
            {"tasapelit": 0, "voitot": 0, "häviöt": 1},
            {"tasapelit": 1, "voitot": 0, "häviöt": 0},
            {"tasapelit": 0, "voitot": 1, "häviöt": 0}
        ]

        for i in range(6):
            self.assertEqual(ai_selector.scores[i], valid_scores_p[i])
            self.assertEqual(ai_selector.stats[i], valid_stats_p[i])

    @patch('ai.BaseAi')
    def test_select_best_ai_valid(self, MockBaseAi):
        mock_base_ai_instance = MagicMock()
        MockBaseAi.side_effect = [mock_base_ai_instance for _ in range(6)]

        ai_selector = AiSelector(5, self.trie_mock)

        for i, model in enumerate(ai_selector.models):
            model.last_seven = ['k', 'p', 's', 'k', 'p', 's', 'k']
            ai_selector.scores[i] = i

        best_ai = ai_selector.select_best_ai()
        self.assertEqual(best_ai, ai_selector.models[5])
