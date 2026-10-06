class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = (R + L) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                L = m + 1
            else:
                R = m - 1

        return -1