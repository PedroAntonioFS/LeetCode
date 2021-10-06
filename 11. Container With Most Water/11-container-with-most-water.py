#Tempo O(n)
#Memória O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:

            h = min(height[left], height[right])
            d = right - left

            if h*d > max_area:
                max_area = h*d

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area