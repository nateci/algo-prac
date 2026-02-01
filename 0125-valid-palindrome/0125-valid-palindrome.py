class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        s = ''.join(cleaned)


        left = 0
        right = len(s) - 1
        while left <= right:
            if s[right] != s[left]:
                return False
            left += 1
            right -= 1
            
        return True