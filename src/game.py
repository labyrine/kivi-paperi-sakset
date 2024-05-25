import random

class RockPaperScissors:
    """Class which runs the game rock-paper-scissors.

    Attributes:
        number_of_rounds: Number of rounds in a game.
        current_round: Indicates which round of the game is currently going.
        player_points: Number of player wins.
        ai_points: Number of machine/ai wins.
        draw: Number of draws.
    """
    def __init__(self):
        """The constructor of the class the RockPaperScissors that sets up the game.
        """
        self.number_of_rounds = 10
        self.curret_round = 0
        self.player_points = 0
        self.ai_points = 0
        self.draw = 0

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
        return True

    def get_ai_choice(self):
        """Placeholder function for getting machines choice to play. Now only randomised.
        """

        x = random.randint(1, 3)
        if x == 1:
            ai_choice = "k"
        elif x == 2:
            ai_choice = "p"
        elif x == 3:
            ai_choice = "s"
        return ai_choice
    
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
