class Node:
    """
    Every node element contains one character, a dictionary of children and a isTerminal
    flag value signifying if the Node character is a terminal character for a word
    """
    def __init__(self,character = None, isTerminal : bool = False) -> None:
      self.character = character
      self.children = {}
      self.isTerminal = isTerminal

class Trie:
    def __init__(self) -> None:
        self.root = Node('')
    
    def insert(self,word:str) -> None:
        """
        This method inserts a word into the trie
        """
        curr = self.root
        for char in word:
            """
            If the current character is not already in the children dict of the node
            pointed by curr, add the character as a child of the curr node.

            Set curr as the child of itself pointed by the current character.
            """
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        """
        After reading the entire word , set the final charachter to which curr is now
        pointing as the terminal character
        """
        curr.isTerminal=True
    
    def __contains__(self,word:str) -> bool:
        """
        This method helps to check if the trie contains a certain word as 
        a valid word (i.e ->  The word ends with a Terminal Character node)
        """
        curr = self.root
        for char in word:
            """
            Whenever even one character of the word is not found, False is returned.
            If the entire word has been traversed and the final character is found to be
            a terminal character , True is returned. Else False is returned.
            """
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isTerminal
    
    def getPrefixes(self,word) -> list:
        """
        This method returns all the possible prefixes of a word already existing in
        the trie
        """
        prefix = ''
        prefixes = []
        curr = self.root
        for char in word:
            """
            Whenever the currently read character is not found within the children of
            the current trie, the prefixes list is returned, else we traverse all the
            characters in the word and keep appending prefix with the current character
            untill we reach a terminal node, where we append the prefixes list with the 
            prefix
            """
            if char not in curr.children:
                return prefixes
            curr = curr.children[char]
            prefix += char
            if curr.isTerminal:
                prefixes.append(prefix)
        return prefixes