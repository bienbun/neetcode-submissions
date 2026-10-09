class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        need = {}
        for letter in t:
            need[letter] = need.get(letter, 0) + 1

        left = 0
        window = {}
        have = 0
        needCount = len(need)

        result = [-1, -1]
        resultLen = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == needCount:
                if right - left + 1 < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left += 1

        if resultLen == float("inf"):
            return ""
        
        leftIndex, rightIndex = result
        return s[leftIndex:rightIndex + 1]