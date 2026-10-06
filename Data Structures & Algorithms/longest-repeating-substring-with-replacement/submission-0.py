class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        L = 0
        maxFreq = 0
        longest = 0

        for R in range(len(s)):
            counter[s[R]] = counter.get(s[R], 0) + 1
            maxFreq = max(maxFreq, counter[s[R]])

            while (R - L + 1) - maxFreq > k:
                counter[s[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)
        
        return longest