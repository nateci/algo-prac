class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        if len(pattern) != len(words):
            return False

        charmap = {}
        wordmap = {}
        for i, (char, word) in enumerate(zip(pattern, words)):
            if char not in charmap:
                charmap[char] = i

            if word not in wordmap:
                wordmap[word] = i

            if wordmap[word] != charmap[char]:
                return False

        return True
