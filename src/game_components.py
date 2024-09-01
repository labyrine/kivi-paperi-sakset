class ScoreManager:
    """Class which manages player's and AI's scores.

    Attributes:
        player_points: Number of player wins.
        ai_points: Number of machine/ai wins.
        draw: Number of draws.
    """
    def __init__(self):
        self.player_points = 0
        self.ai_points = 0
        self.draw = 0

    def who_won(self, players_choice, ai_choice):
        """Function for figuring out who won the round.

        Args:
            players_choice: String containing players choice for round.
            ai_choice: String containing machines choice for round.
        """
        if players_choice == ai_choice:
            self.draw += 1
            return 'Tasapeli'
        if players_choice == "k" and ai_choice == "s":
            self.player_points += 1
            return 'Sinä voitit'
        if players_choice == "s" and ai_choice == "p":
            self.player_points += 1
            return 'Sinä voitit'
        if players_choice == "p" and ai_choice == "k":
            self.player_points += 1
            return 'Sinä voitit'
        self.ai_points += 1
        return 'Pelikone voitti'
    
class LastSevenManager:
    """Class which manages history of palyers choices from 7 previous rounds.

    Attributes:
        last_seven: String for storing the last seven of players choices.
        trie: Data structure for saving strings and substrings.
    """
    def __init__(self, trie):
        self.last_seven = ""
        self.trie = trie

    def update_string(self, players_choice):
        """Function for updatings string last_seven.

        Args:
            players_choice: String containing players choice for round.
        """
        if len(self.last_seven) < 7:
            self.last_seven += players_choice
        else:
            self.last_seven = self.last_seven[1:] + players_choice

    def save_player_choice_to_trie(self):
        """Function for saving every substring of the string to trie if string is 
        at least the lenght of 2 but not longer than 7.
        """
        if len(self.last_seven) >= 2:
            for length in range(2, len(self.last_seven) + 1):
                substring = self.last_seven[-length:]
                self.trie.add(substring)
