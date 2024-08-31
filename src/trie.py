class Node:
    """Class which showcases an entity within a trie data structure.

    Attributes:
        children: Number of different characters that can be used.
        frequency: Tells how many times specific string has been encountered.
    """

    def __init__(self):
        """The constructor for class Node.
        """
        self.children = [None] * 3
        self.frequency = 0


class Trie:
    """Class which makes a trie data structure.

    Attributes:
        root: Number of rounds in a game.
        characters_index: Indicates which round of the game is currently going.
    """

    def __init__(self):
        """The constructor for class Trie.
        """

        self.root = None
        self.characters_index = {'k': 0, 'p': 1, 's': 2}

    def _character_to_index(self, c):
        """Function for converting character to index.

        Args:
            c (String): Character that can be k, p or s.
        """
        return self.characters_index[c]

    def add(self, key):
        """Function for saving string to the data structure.

        Args:
            key (String): String consisting of characters k, p and/or s.
        """

        if self.root is None:
            self.root = Node()

        node = self.root
        for c in key:
            i = self._character_to_index(c)
            if node.children[i] is None:
                node.children[i] = Node()
            node = node.children[i]
        node.frequency += 1

    def get_next_frequencies(self, key):
        """Function for getting the frequencies for the next charaxters after the key string.

        Args:
            key (String): String consisting of characters k, p and/or s.
        """

        if self.root is None:
            return {}

        node = self.root
        for c in key:
            i = self._character_to_index(c)
            if node.children[i] is None:
                return {}
            node = node.children[i]

        frequencies = {}
        characters = 'kps'
        for i in range(3):
            child = node.children[i]
            if child is not None:
                frequencies[characters[i]] = child.frequency
        return frequencies

    def _help_function_get_display(self, node, key, trie_contents):
        """Help function for collecting strings and frequencies of trie by using recursion.

        Args:
           node (Node): Starting point of the trie data structure.
           key (String): String consisting of characters k, p and/or s. Consists of contents up to the current node.
           trie_contents (Tuple): Consists of string and frequency for the string.
        """

        if node is None:
            return

        if node.frequency > 0:
            trie_contents.append((key, node.frequency))

        characters = 'kps'
        for i, child in enumerate(node.children):
            if child is not None:
                self._help_function_get_display(
                    child, key + characters[i], trie_contents)

    def get_all_strings_with_frequencies(self):
        """Function to call _help_function_get_display and to return contents of trie.
        """

        trie_contents = []
        self._help_function_get_display(self.root, "", trie_contents)
        return trie_contents
