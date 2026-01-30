class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counter = {}
        for char in magazine:
            counter[char] = counter.get(char, 0) + 1


        for char in ransomNote:
            if char not in counter or counter[char] == 0:
                return False

            counter[char] -= 1

        return True


        """
        ransom note = aa
        magazine = ab

        """


        

        
        