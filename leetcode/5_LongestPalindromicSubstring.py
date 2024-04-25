"""
Given a string s, return the longest palindromic substring  in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
"""


class Solution(object):
    # bad solution
    def isPalindrom(self, chars_list):
        reversed_chars_list = chars_list[::-1]
        return chars_list == reversed_chars_list
    def longestPalindrome1(self, s):
        res = [s[0]]

        for index, char in enumerate(s):
            chars_list = [char]
            for internal_loop_char in s[index + 1::]:
                chars_list.append(internal_loop_char)
                if self.isPalindrom(chars_list) and len(chars_list) > len(res):
                    res = chars_list[:]

        return ''.join(res)

    def longestPalindrome(self, s):
        res = s[0]
        for index, char in enumerate(s[0:-1]):
            if char == s[index + 1]:
                step = 1
                while index + step < len(s) and s[index] == s[index + step]:
                    step += 1

                res_ = self.is_list_palindrom(s, index, index + step - 1)
            else:
                res_ = self.is_list_palindrom(s, index)
                a = 0
            if len(res_) > len(res):
                res = res_
        return res

    def is_list_palindrom(self, list_, i1, i2=0):
        leftChar = i1
        rightChar = i2
        res = list_[i1:i2 + 1]

        while leftChar > 0 and rightChar < len(list_) - 1:
            if list_[leftChar - 1] == list_[rightChar + 1]:
                res = list_[leftChar - 1: rightChar + 2]
                leftChar -= 1
                rightChar += 1
                a = 0
            else:
                break
        return res




sol = Solution()
# print(sol.longestPalindrome("bahhhhhhha"))
print(sol.longestPalindrome("ffffffrrrrhhwhrrrrr"))
