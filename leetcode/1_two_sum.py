from typing import List

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target - nums[i]) != i:
                res.append(i)
                res.append(nums.index(target - nums[i]))
                break
        return res


sol = Solution()
print(sol.two_sum([3, 2, 4], 6))
