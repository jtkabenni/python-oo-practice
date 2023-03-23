
import random 

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    def __init__(self, path):
        """Initiates word finder machine that generates random word"""
        file = open(path)
        self.dictionary=self.parse(file)
        print(f"{len(self.dictionary)} words read")
    def parse(self, file):
        """Parses text file and returns list of words"""
        return [line.strip() for line in file]
    def random(self):
        """Returns random word from list"""
        word_position = random.randint(0, len(self.dictionary )-1)
        return self.dictionary[word_position]

class SpecialWordFinder(WordFinder):
    """Specialized word finder that includes only words and not items that start with a non letter"""
    def __init__ (self, path):
        super().__init__(path)
    def parse (self, file):
        """Parses text file and returns list of words, skipping non words"""
        letters = "abcdefghijklmnopqrstuvwxyz"
        return [line.strip() for line in file if line[0] in letters or line[0] in letters.upper()]

