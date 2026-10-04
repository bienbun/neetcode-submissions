class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:
                if num + nums[L] + nums[R] > 0:
                    R -= 1
                elif num + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    result.append([num,nums[L],nums[R]])

                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return result