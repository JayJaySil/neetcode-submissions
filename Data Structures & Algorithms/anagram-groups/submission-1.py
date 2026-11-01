class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        keys = defaultdict(list)
        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - ord('a')] += 1

            freq_key = tuple(freq)
            keys[freq_key].append(word)
        return list(keys.values())




        