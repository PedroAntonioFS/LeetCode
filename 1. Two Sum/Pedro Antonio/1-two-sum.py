#Tempo: O(n)
#Memória: O(n).
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if hash_nums.get(complement) != None:
                return [hash_nums.get(complement), i]
            hash_nums[nums[i]] = i