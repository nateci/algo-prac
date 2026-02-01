class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        smap = {}
        for char in s:
            smap[char] = smap.get(char, 0) + 1

        tmap = {}
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1

        return tmap == smap