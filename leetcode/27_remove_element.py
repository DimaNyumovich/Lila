from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return len([x for x in nums if x != val])
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)




print(Solution().removeElement([0,1,2], 2))