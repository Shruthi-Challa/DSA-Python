class Solution(object):
    def wordPattern(self, pattern, s):
        word = s.split(" ")
        if len(pattern) != len(word):
            return False

        wordTochar = {}
        charToword = {}

        for c,w in zip(pattern,word):
            if c in charToword and charToword[c]!=w:
                return False
            if w in wordTochar and wordTochar[w]!=c:
                return False

            charToword[c] = w
            wordTochar[w] = c

        return True