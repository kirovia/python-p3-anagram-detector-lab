# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        if type(word) not in [str]:
            raise ValueError('Word must be a string')
        else:
            self._word = word

    def match(self, list):
        matches_list = []
        for item in list:
            if sorted(item) == sorted(self._word):
                matches_list.append(item)
        return matches_list