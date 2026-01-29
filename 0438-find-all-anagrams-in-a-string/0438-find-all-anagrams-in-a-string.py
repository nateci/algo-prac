class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        result = []


        freq_p = {}
        for char in p:
            freq_p[char] = freq_p.get(char, 0) + 1

        window_count = {}
        for i in range(len(p)):
            char = s[i]
            window_count[char] = window_count.get(char, 0) + 1


        if window_count == freq_p:
            result.append(0)


        for i in range(len(p), len(s)):
            new_char = s[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            old_char = s[i - len(p)]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

            if window_count == freq_p:
                result.append(i - len(p) + 1)

        return result
        

            
        