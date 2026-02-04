class Solution:
    def groupAnagrams(self, strs):
        group = {}
        
        for word in strs:
            count = [0] * 26  # For a-z
            
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        
        return list(group.values())