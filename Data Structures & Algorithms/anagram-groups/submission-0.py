class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            alphabet = [0] * 26

            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1
            
            key = tuple(alphabet)

            if key not in result:
                result[key] = []

            result[key].append(word)

        return list(result.values())