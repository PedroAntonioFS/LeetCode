from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        begin = [0,0,0]
        end = [0,len(nums1)-1,len(nums2)-1]
        
        while True:
            test_begin = ((begin[1] <= end[1]) and ((begin[2] > end[2]) or (nums1[begin[1]] < nums2[begin[2]])))
            test_end = ((begin[1] <= end[1]) and ((begin[2] > end[2]) or (nums1[end[1]] > nums2[end[2]])))

            begin = [1,begin[1]+1,begin[2]] if test_begin else [2,begin[1],begin[2]+1]
            end = [1,end[1]-1,end[2]] if test_end else [2,end[1],end[2]-1]

            if (begin[1] > end[1]) and (begin[2] > end[2]):
                break

        v1 = nums1[begin[1]-1] if begin[0] == 1 else nums2[begin[2]-1]
        v2 = nums1[end  [1]+1] if end  [0] == 1 else nums2[end  [2]+1]
        return (v1+v2)/2