class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazineFreq = {}

        for char in magazine:
            magazineFreq[char] = magazineFreq.get(char, 0) + 1

        
        for char in ransomNote:
            if char not in magazineFreq or magazineFreq[char] == 0:
                return False
                
            magazineFreq[char] -= 1

        return True

        
        