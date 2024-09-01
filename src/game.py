from trie import Trie
from ai import AiSelector
from game_components import ScoreManager, LastSevenManager


class RockPaperScissors:
    """Class which runs the game rock-paper-scissors.

    Attributes:
        number_of_rounds: Number of rounds in a game.
        current_round: Indicates which round of the game is currently going.
        score_manager: Class for managing player's and AI's scores.
        trie: Data structure for saving strings and substrings.
        ai_selector: Class that compares different Ai models performance and 
        chooses most suitable one.
        last_seven_manager: Class for history of palyers choices from 7 previous rounds.
    """

    def __init__(self):
        """The constructor of the class the RockPaperScissors that sets up the game.
        """
        self.number_of_rounds = 50
        self.curret_round = 0
        self.score_manager = ScoreManager()
        self.trie = Trie()
        self.ai_selector = AiSelector(15, self.trie)
        self.last_seven_manager = LastSevenManager(self.trie)

    def start(self):
        """Function for starting the game and handling ending display of the game.
        """

        print("Tervetuloa peliin")
        print("Pelissä on", self.number_of_rounds, "kierrosta")
        while self.curret_round < self.number_of_rounds:
            if not self.round():
                break

        print("Peli päättyi")
        print("Pelaaja voitti", self.score_manager.player_points, "kertaa")
        print("Pelikone voitti", self.score_manager.ai_points, "kertaa")
        print("Tasapeli tapahtui", self.score_manager.draw, "kertaa")
        print("AI:n voittoprosentti:", round(
            (self.score_manager.ai_points / self.number_of_rounds) * 100, 1), "%")
        print()

    def round(self):
        """Function for handling one round of the game.
        """

        self.curret_round += 1
        print("Kierros:", self.curret_round)
        players_choice = self.get_player_choice()
        ai_choice = self.ai_selector.play_ai()
        result = self.score_manager.who_won(players_choice, ai_choice)
        print("Sinä valitsit", players_choice)
        print("Pelikone valitsi", ai_choice)
        print(result)
        self.last_seven_manager.update_string(players_choice)
        self.last_seven_manager.save_player_choice_to_trie()
        self.ai_selector.update_last_seven(self.last_seven_manager.last_seven)
        self.ai_selector.update_scores()
        self.ai_selector.select_best_ai()
        self.ai_selector.print_model_stats()
        print(
            f"Mallien pisteet seuraavalle kierrokselle {self.ai_selector.create_model_scores()}")
        print()
        return True

    def get_player_choice(self):
        """Function for getting players choice to play.
        """

        while True:
            players_choice = input(
                "Valitse kivi (k), paperi (p) tai sakset (s)")
            if players_choice in ['k', 'p', 's'] and len(players_choice) == 1:
                break
            print("Syötä vain kirjain k, p tai s")

        return players_choice
