import random
from trie import Trie

class RockPaperScissors:
    """Class which runs the game rock-paper-scissors.

    Attributes:
        number_of_rounds: Number of rounds in a game.
        current_round: Indicates which round of the game is currently going.
        player_points: Number of player wins.
        ai_points: Number of machine/ai wins.
        draw: Number of draws.
        last_seven: String for storing the last seven of players choices.
        trie: Data structure for saving strings and substrings.
    """
    def __init__(self):
        """The constructor of the class the RockPaperScissors that sets up the game.
        """
        self.number_of_rounds = 10
        self.curret_round = 0
        self.player_points = 0
        self.ai_points = 0
        self.draw = 0
        self.last_seven = ""
        self.trie = Trie()

    def start(self):
        """Function for starting the game and handling ending display of the game.
        """

        print("Tervetuloa peliin")
        while self.curret_round < self.number_of_rounds:
            if not self.round():
                break

        print("Peli päättyi")
        print("Pelaaja voitti", self.player_points, "kertaa")
        print("Pelikone voitti", self.ai_points, "kertaa")
        print("Tasapeli tapahtui", self.draw, "kertaa")

    def round(self):
        """Function for handling one round of the game.
        """

        self.curret_round += 1
        players_choice = self.get_player_choice()
        ai_choice = self.get_ai_choice()
        result = self.who_won(players_choice, ai_choice)
        print("Pelikone valitsi", ai_choice)
        print(result)
        self.create_string(players_choice)
        self.save_player_choice()
        return True

    def get_ai_choice(self):
        """Test version of function for getting machines choice to play. Mix of randomization and using frequency for strings which have length of two.
        """

        if len(self.last_seven) < 2:
            x = random.randint(1, 3)
            if x == 1:
                ai_choice = "k"
            elif x == 2:
                ai_choice = "p"
            elif x == 3:
                ai_choice = "s"
            return ai_choice
        else:
            max_frequency = self.get_max_frequency_for_two()
            if max_frequency == "k":
                ai_choice = "p"
            elif max_frequency == "p":
                ai_choice = "s"
            elif max_frequency == "s":
                ai_choice = "k"
            else:
                x = random.randint(1, 3)
                if x == 1:
                    ai_choice = "k"
                elif x == 2:
                    ai_choice = "p"
                elif x == 3:
                    ai_choice = "s"
                return ai_choice
            return ai_choice
    
    def get_max_frequency_for_two(self):
        """Function for getting the next max frequency for strings which have the length of two.
        """

        if len(self.last_seven) < 2:
            return ""
        frequencies = self.trie.get_next_frequencies(self.last_seven[-2:])
        if frequencies:
            most_frequent_player_move = max(frequencies, key=lambda k: frequencies.get(k))
            return most_frequent_player_move
        return ""
        
    def get_player_choice(self):
        """Function for getting players choice to play.
        """

        while True:
            players_choice = input("Valitse kivi (k), paperi (p) tai sakset (s)")
            if players_choice in ['k', 'p', 's']:
                break
            else:
                print("Syötä vain kirjain k, p tai s")

        return players_choice
    
    def create_string(self, players_choice):
        """Function for updatings string last_seven.

        Args:
            players_choice (String): Players choice for round.
        """

        if len(self.last_seven) < 7:
            self.last_seven += players_choice
        else:
            self.last_seven = self.last_seven[1:] + players_choice
    
    def save_player_choice(self):
        """Function for saving every substring of the string to trie if string is at least the lenght of 2 but not longer than 7.
        """

        if len(self.last_seven) >= 2:
            for length in range(2, len(self.last_seven) + 1):
                substring = self.last_seven[-length:]
                self.trie.add(substring)
        

    def who_won(self, players_choice, ai_choice):
        """Function for figuring out who won the round.

        Args:
            players_choice (String): Players choice for round.
            ai_choice (String): Machines choice for round.
        """

        if players_choice == ai_choice:
            self.draw += 1
            return 'Tasapeli'
        elif players_choice == "k" and ai_choice == "s":
            self.player_points +=1
            return 'Sinä voitit'
        elif players_choice == "s" and ai_choice == "p":
            self.player_points +=1
            return 'Sinä voitit'
        elif players_choice == "p" and ai_choice == "k":
            self.player_points +=1
            return 'Sinä voitit'
        else:
            self.ai_points +=1
            return 'Pelikone voitti'
