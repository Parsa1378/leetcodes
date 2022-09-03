class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, value in enumerate(nums):     
            rem = target - nums[i]
            if rem in dic:
                return [i,dic[rem]]
            else:
                dic[value]=i
        