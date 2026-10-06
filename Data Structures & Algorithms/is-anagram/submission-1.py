class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = {}

        for letter in s:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

        for letter in t:
            if letter not in counter:
                return False

            counter[letter] -= 1

            if counter[letter] < 0:
                return False
        
        return True
