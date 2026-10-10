class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = {}

        for letter in t:
            need[letter] = need.get(letter, 0) + 1

        window = {}
        left, have, needCount = 0, 0, len(need)
        result = [-1,-1]
        resultLen = float("inf")
        
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            while have == needCount:
                if (right - left + 1) < resultLen:
                    resultLen = right - left + 1
                    result = [left,right]
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1
        leftIndex, rightIndex = result

        if resultLen == float("inf"):
            return ""

        return s[leftIndex:rightIndex + 1]

   