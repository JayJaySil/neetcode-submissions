class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = []
        for index, char in enumerate(s):
            if str.isalnum(char):
                string.append(char.lower())
        reverse = []
        for char in string:
            reverse.insert(0, char)
        
        if reverse == string:
            return True
        return False
        