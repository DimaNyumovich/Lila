from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = list(set(nums))
        return len(nums)


print(Solution().removeDuplicates([1,1,2]))