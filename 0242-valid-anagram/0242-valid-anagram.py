class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        for char in t:
            freq_s[char] = freq_s.get(char, 0) - 1



        for count in freq_s.values():
            if count != 0:
                return False

        return True


        



        
        