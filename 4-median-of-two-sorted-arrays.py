from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        biggest, smallest = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)
        total_lenght = len(biggest) + len(smallest)
        half = total_lenght // 2

        left = 0
        right = len(smallest) - 1
        while True: 
            smallest_middle = (right + left) // 2
            biggest_middle = half - smallest_middle - 2
            
            smallest_left_cut = smallest[smallest_middle] if smallest_middle >= 0 else float("-infinity")
            smallest_right_cut = smallest[smallest_middle + 1] if smallest_middle + 1 < len(smallest) else float("infinity")
            biggest_left_cut = biggest[biggest_middle] if biggest_middle >= 0 else float("-infinity")
            biggest_right_cut = biggest[biggest_middle + 1] if biggest_middle + 1 < len(biggest) else float("infinity")

            if (smallest_left_cut <= biggest_right_cut ) and (biggest_left_cut <= smallest_right_cut):
                break
            elif smallest_left_cut > biggest_right_cut:
                right = smallest_middle - 1
            else:
                left = smallest_middle + 1
        
        if total_lenght % 2:
            return min(smallest_right_cut, biggest_right_cut)
        else:
            return (max(smallest_left_cut, biggest_left_cut) + min(smallest_right_cut, biggest_right_cut))/2