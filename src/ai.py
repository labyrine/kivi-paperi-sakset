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

    def predict_ai_choice(self):
        """Function for predicting what player might chooce on next round with 
        frequencies and then returning counter move for that by calling counter_move function.
        """
        if len(self.last_seven) < self.length:
            return ""
        frequencies = self.trie.get_next_frequencies(
            self.last_seven[-self.length:])
        if frequencies:
            most_frequent_player_move = max(
                frequencies, key=frequencies.get)
            ai_choice = self.counter_move(most_frequent_player_move)
            return ai_choice
        return ""

    def counter_move(self, choice):
        """Function for the model to choose best move against the prediction of players choice.
        """
        if choice == "k":
            return "p"
        if choice == "p":
            return "s"
        if choice == "s":
            return "k"
        raise ValueError(f"Virheellinen valinta: {choice}")


class AiSelector:
    def __init__(self, focus_length, trie):
        """The constructor for class AiSelector.

        Attributes:
        focus_length: Number that tells how long the string that the AI model will process is.
        trie: Data structure for saving strings and substrings.
        models: List of the AI models.
        best_model: Holds the current best performing AI model.
        focus_length_scores: A list containing focus_length number of lists. Those lists tell AI 
        models points based on how they well they have performed on last focus lenght number of 
        rounds.
        focus_length_stats: A list containing focus_length number of lists to track the 
        statistics for each model.
        Each of those lists contains a list of list of wins, losses and dwars from a spesific 
        round within focus lenght number of previous rounds.
        """
        self.focus_length = focus_length
        self.trie = trie
        last_seven = ""
        self.models = [BaseAi(length, trie, last_seven)
                       for length in range(1, 7)]
        self.best_model = self.models[0]
        self.focus_length_scores = []
        self.focus_length_stats = []

    def update_last_seven(self, last_seven):
        """Function for updating string last_seven.

        Args:
            last_seven: String to store the last seven of players choices.
        """
        for model in self.models:
            model.last_seven = last_seven

    def update_scores(self):
        """Function for updating scores depending on players input. Also manages that 
        focus_length_scores and focus_length_stats have at most focus_length number of items.
        """
        if len(self.models[0].last_seven) < 2:
            self.focus_length_scores.append([0] * 6)
            return

        players_last_move = self.models[0].last_seven[-1]
        scores = [0] * 6
        stats = [[0, 0, 0] for _ in self.models]
        predictions = [model.predict_ai_choice() for model in self.models]
        print(
            f"Ennusteet seuraavalle kierrokselle jokaiselta mallilta {predictions}")
        for i, prediction in enumerate(predictions):
            if not prediction:
                continue
            if prediction == players_last_move:
                stats[i][2] += 1
            elif (
                (prediction == "k" and players_last_move == "p") or
                (prediction == "p" and players_last_move == "s") or
                (prediction == "s" and players_last_move == "k")
            ):
                scores[i] -= 1
                stats[i][1] += 1
            elif (
                (players_last_move == "k" and prediction == "p") or
                (players_last_move == "p" and prediction == "s") or
                (players_last_move == "s" and prediction == "k")
            ):
                scores[i] += 1
                stats[i][0] += 1
        self.manage_scores_length(scores)
        self.manage_stats_length(stats)

    def manage_scores_length(self, scores):
        """Function for managing that focus_length_scores has at most focus_length 
        number of items from previous focus length rounds.
        """
        self.focus_length_scores.append(scores)
        if len(self.focus_length_scores) > self.focus_length:
            self.focus_length_scores.pop(0)

    def manage_stats_length(self, stats):
        """Function for managing that focus_length_stats has at most focus_length 
        number of items from previous focus length rounds.
        """
        self.focus_length_stats.append(stats)
        if len(self.focus_length_stats) > self.focus_length:
            self.focus_length_stats.pop(0)

    def create_model_scores(self):
        """Function for adding up scores from previous rounds.
        """
        summed_scores = [0] * len(self.focus_length_scores[0])
        for score_list in self.focus_length_scores:
            for i, _ in enumerate(summed_scores):
                summed_scores[i] += score_list[i]
        return summed_scores

    def create_model_stats(self):
        """Function for adding up stats from previous rounds for displaying stats.
        """
        summed_stats = [[0, 0, 0] for _ in range(len(self.models))]
        for stat_list in self.focus_length_stats:
            for i, stat in enumerate(summed_stats):
                for j in range(3):
                    stat[j] += stat_list[i][j]
        return summed_stats

    def select_best_ai(self):
        """Function for selecting best AI model. It selects the model which has the 
        biggest score within focus_length rounds. It gets the scores by calling 
        function create_model_scores().
        """
        scores = self.create_model_scores()
        best_model_index = scores.index(max(scores))
        print(
            f"Valittu paras malli AI{self.models[best_model_index].length} seuraavalle kierrokselle"
            )
        self.best_model = self.models[best_model_index]

    def play_ai(self):
        """Function for running the best AI model.
        """
        prediction = self.best_model.predict_ai_choice()
        if prediction:
            print(
                f"Ai valinta perustuen parhaaseen malliin AI{self.best_model.length}: {prediction}")
            return prediction
        ai_choice = random.choice(["k", "p", "s"])
        print(
            f"Randomisoitu valinta, kun valitun mallin ennustetta ei löytynyt: {ai_choice}")
        return ai_choice

    def print_model_stats(self):
        """Function for printing the statistics of each model which have been compiled 
        from previous focus length rounds. It gets the stats by calling function 
        create_model_stats().
        """
        stats = self.create_model_stats()
        print(
            f"Mallien statistiikat viimeiseltä {self.focus_length} kierrokselta (tai vähemmmän):")
        for i, model_stats in enumerate(stats):
            print(
                f'malli{i+1}: Voitot: {model_stats[0]}, '
                f'Häviöt: {model_stats[1]}, '
                f'Tasapelit: {model_stats[2]}')
