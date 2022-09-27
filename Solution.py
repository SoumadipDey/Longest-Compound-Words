import Trie as T
from collections import deque
import time

class Solution:
    def __init__(self) -> None:
      self.trie = T.Trie()
      self.queue = deque()

    def buildTrie(self,filePath : str = None) -> None:
        """
        Builds the trie. 
        """
        try:
            with open(filePath, mode = 'r') as f:
                for line in f:
                    """
                    Strip the Endl charachter from the end of each word and try to find
                    the prefixes of the word if any within the trie.
                    
                    If prefixes are found, simply divide the word into its respective
                    suffix and enter the (word,suffix) into the deque.

                    Finally Insert the word into the trie.
                    """
                    word = line.rstrip('\n')
                    prefixes = self.trie.getPrefixes(word)
                    for prefix in prefixes:
                        self.queue.append((word, word[len(prefix):]))
                    self.trie.insert(word)
        except:
            print("There was some error with the file!")
            exit(0)
    
    def findLongestCompoundWords(self) -> tuple:
        """
        Finds the longest and second longest compound words within the trie
        and returns them as a tuple (longest, secondLongest)
        """
        longest_word = ''
        longest_length = 0
        second_longest = ''
        #Iterate the dequeue while it is not empty
        while self.queue:
            #Pop out the first tuple from the front side of the dequeue
            #In this way only the compound words are taken into account
            word, suffix = self.queue.popleft()
            """
            If the suffix of the word is a valid word already present in the trie and
            the length of the word is greater than the previous longest length
            change the second longest and longest word and record the new longest length
            """
            if suffix in self.trie and len(word) > longest_length:
                second_longest = longest_word
                longest_word = word
                longest_length = len(word)
            else:
                """
                Else get the possible prefixes for the suffix of the word.
                If prefixes are found, simply divide the word into its respective
                suffix and enter the (word,suffix) into the deque.
                """ 
                prefixes = self.trie.getPrefixes(suffix)
                for prefix in prefixes:
                    self.queue.append((word, suffix[len(prefix):]))

        return (longest_word,second_longest)

if __name__ == "__main__":
    sol = Solution()
    start = time.time()
    sol.buildTrie("Input_02.txt")
    first,second = sol.findLongestCompoundWords()
    end = time.time()
    print("Longest Compound Word:",first)
    print("Second Longest Compound Word:",second)
    print("Time taken: ",str(end - start), "seconds")