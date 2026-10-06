class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanText = ""
        reversedText = ""

        for char in s:
            if char.isalnum():
                cleanText += char.lower()

        for char in cleanText:
            reversedText = char + reversedText

        if cleanText == reversedText:
            return True
        else:
            return False
        