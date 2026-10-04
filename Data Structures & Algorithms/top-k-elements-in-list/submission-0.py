class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for key, frequency in counter.items():
            freq[frequency].append(key)
        
        result = []

        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]:
                result.append(num)

            if len(result) == k:
                return result