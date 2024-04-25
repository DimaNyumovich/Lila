"""
Given a string s, find the length of the longest
substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        list_res = []
        for char in s:
            if char not in list_res:
                list_res.append(char)
            else:
                list_res = list_res[list_res.index(char) + 1::]
                list_res.append(char)
            if len(list_res) > res:
                res = len(list_res)
        return res


sol = Solution()
# print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring('abaabl'))