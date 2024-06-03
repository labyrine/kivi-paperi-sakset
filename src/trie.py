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

    def search(self, key):
        """Function for searchin a string.

        Args:
            key (String): String consisting of characters k, p and/or s.
        """

        if self.root is None:
            return 0

        node = self.root
        for c in key:
            i = self._character_to_index(c)
            if node.children[i] is None:
                return 0
            node = node.children[i]
        return node.frequency

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

    def delete(self, key):
        """Function for deleting a string from the data structure which calls a another function.

        Args:
            key (String): String consisting of characters k, p and/or s.
        """

        if self.root is not None:
            self.root = self._delete_help_function(self.root, key, 0)

    def _delete_help_function(self, node, key, depth):
        """Help function for deleting a string from the data structure by using recursion.

        Args:
            node (Node): Starting point of the trie data structure.
            key (String): String consisting of characters k, p and/or s.
            depth (Integer): The current depth in the trie data structure.
        """

        if node is None:
            return None

        if depth == len(key):
            if node.frequency > 0:
                node.frequency -= 1

            if node.frequency == 0:
                all_are_none = True
                for child in node.children:
                    if child is not None:
                        all_are_none = False
                        break
                if all_are_none:
                    return None
            return node

        index = self._character_to_index(key[depth])
        node.children[index] = self._delete_help_function(
            node.children[index], key, depth + 1)

        if node.frequency == 0:
            all_are_none = True
            for child in node.children:
                if child is not None:
                    all_are_none = False
                    break
            if all_are_none:
                return None
        return node
