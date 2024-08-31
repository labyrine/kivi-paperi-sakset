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
        self.assertEqual(ai.predict_ai_choice(), "k")

    def test_prediction_short(self):
        ai = BaseAi(self.length, self.trie_mock, self.last_seven2)
        self.assertEqual(ai.predict_ai_choice(), "")

    def test_prediction_empty(self):
        ai = BaseAi(2, self.trie_mock, self.last_seven1)
        self.assertEqual(ai.predict_ai_choice(), "")

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
        mock_base_ai_instance.predict_ai_choice.side_effect = [
            "k", "p", "s", "k", "p", "s"]
        MockBaseAi.side_effect = [mock_base_ai_instance for _ in range(6)]
        
        ai_selector = AiSelector(5, self.trie_mock)
        ai_selector.update_last_seven("kpppssp")
        ai_selector.update_scores()

        valid_scores = [-1, 0, 1, -1, 0, 1]
        valid_stats = [[[0, 1, 0], [0, 0, 1], [
            1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]]]

        self.assertEqual(ai_selector.focus_length_scores[0], valid_scores)
        self.assertEqual(ai_selector.focus_length_stats, valid_stats)

    @patch('ai.BaseAi')
    def test_select_best_ai_valid(self, MockBaseAi):
        mock_base_ai_instance = MagicMock()
        MockBaseAi.side_effect = [mock_base_ai_instance for _ in range(6)]

        ai_selector = AiSelector(5, self.trie_mock)

        for i in range(6):
            ai_selector.focus_length_scores.append([i])

        ai_selector.select_best_ai()
        self.assertEqual(ai_selector.best_model, ai_selector.models[5])
