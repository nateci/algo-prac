class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        
        patternmap = {}
        smap = {}

        for i in range(len(words)):
            if pattern[i] not in patternmap:
                patternmap[pattern[i]] = i

            if words[i] not in smap:
                smap[words[i]] = i

            if smap[words[i]] != patternmap[pattern[i]]:
                return False

        return True
                


        