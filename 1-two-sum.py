from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        begin = 0
        end = len(nums)-1

        hash_nums = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if hash_nums.get(complement) != None:
                return [hash_nums.get(complement), i]
            hash_nums[nums[i]] = i

instance = Solution

print(instance.twoSum(Solution,nums=[2,7,11,15], target=9))
