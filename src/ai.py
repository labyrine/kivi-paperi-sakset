import random


class Ai1:
    def __init__(self, trie, last_seven):
        """The constructor for class Ai1.

        Attributes:
        length: Tells how long the string tha the AI will process.
        trie: Data structure for saving strings and substrings.
        last_seven: String for storing the last seven of players choices.
        """

        self.length = 1
        self.trie = trie
        self.last_seven = last_seven

    def prediction(self):
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=lambda k: frequencies.get(k))
            return self.counter_move(most_frequent_player_move)
        return ""

    def counter_move(self, choice):
        if choice == "k":
            return "p"
        elif choice == "p":
            return "s"
        elif choice == "s":
            return "k"


class Ai2:
    def __init__(self, trie, last_seven):
        """The constructor for class Ai2.
        """
        self.length = 2
        self.trie = trie
        self.last_seven = last_seven

    def prediction(self):
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=lambda k: frequencies.get(k))
            return self.counter_move(most_frequent_player_move)
        return ""

    def counter_move(self, choice):
        if choice == "k":
            return "p"
        elif choice == "p":
            return "s"
        elif choice == "s":
            return "k"


class Ai3:
    def __init__(self, trie, last_seven):
        """The constructor for class Ai3.
        """
        self.length = 3
        self.trie = trie
        self.last_seven = last_seven

    def prediction(self):
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=lambda k: frequencies.get(k))
            return self.counter_move(most_frequent_player_move)
        return ""

    def counter_move(self, choice):
        if choice == "k":
            return "p"
        elif choice == "p":
            return "s"
        elif choice == "s":
            return "k"


class Ai4:
    def __init__(self, trie, last_seven):
        """The constructor for class Ai5.
        """
        self.length = 4
        self.trie = trie
        self.last_seven = last_seven

    def prediction(self):
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=lambda k: frequencies.get(k))
            return self.counter_move(most_frequent_player_move)
        return ""

    def counter_move(self, choice):
        if choice == "k":
            return "p"
        elif choice == "p":
            return "s"
        elif choice == "s":
            return "k"


class Ai5:
    def __init__(self, trie, last_seven):
        """The constructor for class Ai5.
        """
        self.length = 5
        self.trie = trie
        self.last_seven = last_seven

    def prediction(self):
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=lambda k: frequencies.get(k))
            return self.counter_move(most_frequent_player_move)
        return ""

    def counter_move(self, choice):
        if choice == "k":
            return "p"
        elif choice == "p":
            return "s"
        elif choice == "s":
            return "k"


class Ai6:
    def __init__(self, trie, last_seven):
        """The constructor for class Ai6.
        """
        self.length = 6
        self.trie = trie
        self.last_seven = last_seven

    def prediction(self):
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=lambda k: frequencies.get(k))
            return self.counter_move(most_frequent_player_move)
        return ""

    def counter_move(self, choice):
        if choice == "k":
            return "p"
        elif choice == "p":
            return "s"
        elif choice == "s":
            return "k"


class AiSelector:
    def __init__(self, focus_length, last_seven, trie):
        """The constructor for class multi ai.

        Attributes:
        scores: Tells how long the string tha the AI will process.
        last_seven: String for storing the last seven of players choices.
        trie: Data structure for saving strings and substrings.
        mod1: AI-model 1.
        mod2:AI-model 2.
        mod3: AI-model 3.
        mod4: AI-model 4
        mod5: AI-model 5.
        mod6: AI-model 6
        models: List of the AI models.
        stats: A list containing dictionaries to track the statistics for each model in the AI. 
        """

        self.scores = [0] * 6
        self.focus_length = focus_length
        self.last_seven = last_seven
        self.trie = trie
        self.mod1 = Ai1(trie, last_seven)
        self.mod2 = Ai2(trie, last_seven)
        self.mod3 = Ai3(trie, last_seven)
        self.mod4 = Ai4(trie, last_seven)
        self.mod5 = Ai5(trie, last_seven)
        self.mod6 = Ai6(trie, last_seven)
        self.models = [self.mod1, self.mod2,
                       self.mod3, self.mod4, self.mod5, self.mod6]
        self.stats = [{"voitot": 0, "häviöt": 0, "tasapelit": 0}
                      for _ in self.models]

    def update_scores(self, players_actual_move):
        """Function for updatings string last_seven.

        Args:
            players_actual_move (String): Players choice for the round.
        """

        predictions = [model.prediction() for model in self.models]
        for i, prediction in enumerate(predictions):
            if prediction == players_actual_move:
                self.stats[i]["tasapelit"] += 1
            elif (prediction == "k" and players_actual_move == "p") or (prediction == "p" and players_actual_move == "s") or (prediction == "s" and players_actual_move == "k"):
                self.scores[i] -= 1
                self.stats[i]["häviöt"] += 1
            elif (players_actual_move == "k" and prediction == "p") or (players_actual_move == "p" and prediction == "s") or (players_actual_move == "s" and prediction == "k"):
                self.scores[i] -= 1
                self.stats[i]["voitot"] += 1

    def select_best_ai(self):
        """Function for selecting best AI by finding the model which has the best score.
        """
        focus_choices = self.last_seven[-self.focus_length:]
        ai_scores = []
        for i in range(len(self.scores)):
            model_score = self.scores[i]
            model = self.models[i]
            if model.last_seven[-self.focus_length:] == focus_choices:
                ai_scores.append(model_score)

        if ai_scores:
            best_model_index = ai_scores.index(max(ai_scores))
            return self.models[best_model_index]
        else:
            print("Tapahtui virhe valittaessa sopivaa AI:ta")

    def play_ai(self):
        """Function for running the best AI at the moment.
        """
        if len(self.last_seven) < 7:
            x = random.randint(1, 3)
            if x == 1:
                ai_choice = "k"
            elif x == 2:
                ai_choice = "p"
            elif x == 3:
                ai_choice = "s"
            return ai_choice
        best_model = self.select_best_ai()
        return best_model.prediction()

    def print_stats(self):
        """Function for printing the statistics of each model.
        """
        for i, model_stats in enumerate(self.stats):
            print(
                f'mod{i+1}: Voitot: {model_stats["voitot"]}, Häviöt: {model_stats["häviöt"]}, Tasapelit: {model_stats["tasapelit"]}')
