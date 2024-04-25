# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


class Solution:
    def isPalindrome(self, x: int)-> bool:
        res1 = str(x)
        res2 = ''.join(list(res1)[::-1])
        return res1 == res2

sol = Solution()
print(sol.isPalindrome(121))