from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        begin = 0
        end = len(nums)-1

        nums_sorted = sorted(nums)
        while True:
            if nums_sorted[begin] + nums_sorted[end] == target:
                break
            elif nums_sorted[begin] + nums_sorted[end] > target:
                end -= 1
            else:
                begin += 1

        sol = []
        index = 0
        while len(sol) < 2:
            if (nums[index] == nums_sorted[begin]) and (nums[index] != nums_sorted[end]):
                sol.append(index)
            elif nums[index] == nums_sorted[end]:
                sol.append(index)
            index += 1
        
        return sol

instance = Solution

print(instance.twoSum(Solution,nums=[3,2,3], target=6))
