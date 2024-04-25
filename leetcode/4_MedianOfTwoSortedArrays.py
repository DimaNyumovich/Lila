"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

# bad solution
class Solution(object):
    def findMedianSortedArrays1(self, nums1, nums2):
        res = (nums1 + nums2)
        res.sort()
        print(res)
        if len(res) % 2 == 1:
            return res[len(res) // 2]
        else:
            return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        merged_list = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                merged_list.append(nums1.pop(0))
            else:
                merged_list.append(nums2.pop(0))
        merged_list = merged_list + nums1 + nums2


        n = len(merged_list)
        if n % 2 == 0:
            # If the length of the merged array is even
            return float(merged_list[n // 2 - 1] + merged_list[n // 2]) / 2
        else:
            # If the length of the merged array is odd
            return merged_list[n // 2]



sol = Solution()
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
