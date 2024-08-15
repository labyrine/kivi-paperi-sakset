import random


class BaseAi:
    def __init__(self, length, trie, last_seven):
        """The constructor for class base class AI.

        Attributes:
        length: Tells how long the string tha the AI will process.
        trie: Data structure for saving strings and substrings.
        last_seven: String for storing the last seven of players choices.
        """

        self.length = length
        self.trie = trie
        self.last_seven = last_seven

    def prediction(self):
        """Function for predictiong what player might chooce on next round with frequencies.
        """
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=lambda k: frequencies.get(k))
            prediction = self.counter_move(most_frequent_player_move)
            return prediction
        return ""

    def counter_move(self, choice):
        """Function for the AI to choose best thing against the prediction of players choice.
        """
        if choice == "k":
            return "p"
        elif choice == "p":
            return "s"
        elif choice == "s":
            return "k"


class AiSelector:
    def __init__(self, focus_length, trie):
        """The constructor for class AiSelector.

        Attributes:
        scores: Points for all the AIs based on how they well they do.
        focus_length: Tells how long the string that the AI will process is.
        trie: Data structure for saving strings and substrings.
        models: List of the AI models.
        stats: A list containing dictionaries to track the statistics for each model in the AI. 
        """

        self.scores = [0] * 6
        self.focus_length = focus_length
        self.trie = trie
        last_seven = ""
        self.models = [BaseAi(length, trie, last_seven)
                       for length in range(1, 7)]
        self.stats = [{"voitot": 0, "häviöt": 0, "tasapelit": 0}
                      for _ in self.models]

    def update_last_seven(self, last_seven):
        """Function for updating string last_seven.

        Args:
            last_seven (String): Place to store the last seven of players choices.
        """
        for model in self.models:
            model.last_seven = last_seven

    def update_scores(self, players_actual_move):
        """Function for updating scores.

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
                self.scores[i] += 1
                self.stats[i]["voitot"] += 1

    def select_best_ai(self):
        """Function for selecting best AI by finding the model which has the best score.
        """
        focus_choices = self.models[0].last_seven[-self.focus_length:]
        ai_scores = []
        for i in range(len(self.scores)):
            model_score = self.scores[i]
            model = self.models[i]
            if model.last_seven[-self.focus_length:] == focus_choices:
                ai_scores.append(model_score)

        if ai_scores:
            best_model_index = ai_scores.index(max(ai_scores))
            print(f"Valittu paras AI{self.models[best_model_index].length}") # Print
            return self.models[best_model_index]
        else:
            print("Tapahtui virhe valittaessa sopivaa AI:ta")

    def play_ai(self):
        """Function for running the best AI at the moment.
        """
        if len(self.models[0].last_seven) < 7:
            ai_choice = random.choice(["k", "p", "s"])
            print(f"Randomisoitu valinta, kun ei ei etsitty tai löydetty sopivaa AI:ta: {ai_choice}") # Print
            return ai_choice
        best_model = self.select_best_ai()
        prediction = best_model.prediction()
        if prediction:
            print(f"Ai valinta perustuen parhaaseen malliin AI{best_model.length}: {prediction}") # Print
            return prediction
        ai_choice = random.choice(["k", "p", "s"])
        print(f"Randomisoitu valinta, kun valitun AI:n ennustetta ei löytynyt: {ai_choice}") # Print
        return ai_choice

    def print_ai_stats(self):
        """Function for printing the statistics of each model.
        """
        print(f"Mallien statistiikat:")
        for i, model_stats in enumerate(self.stats):
            print(
                f'malli{i+1}: Voitot: {model_stats["voitot"]}, Häviöt: {model_stats["häviöt"]}, Tasapelit: {model_stats["tasapelit"]}')
