class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        keys = {}
        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - ord('a')] += 1

            freq_key = tuple(freq)
            if freq_key in keys:
                keys[freq_key].append(word)
            else:
                keys[freq_key] = [word]
        for strings in keys.values():
            groups.append(strings)
        return groups




        