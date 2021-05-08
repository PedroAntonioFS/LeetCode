from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        begin1 = begin2 = beging = endg = 0
        end1 = len(nums1)-1
        end2 = len(nums2)-1

        pair = True
        while (end1 >= begin1) or (end2 >= begin2):
            if pair:
                if nums1[begin1] < nums2[begin2]:
                    beging = nums1[begin1]
                    begin1 += 1
                else:
                    beging = nums2[begin2]
                    begin2 += 1
            else:
                if nums1[end1] > nums2[end2]:
                    endg = nums1[end1]
                    end1 -= 1
                else:
                    endg = nums2[end2]
                    end2 -= 1
            pair = not pair
        if pair:
            return (beging+endg)/2
        else:
            return beging

sol = Solution()

print(sol.findMedianSortedArrays([0,0], [0,0]))