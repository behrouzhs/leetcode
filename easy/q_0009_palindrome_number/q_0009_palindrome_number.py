# URL: https://leetcode.com/problems/palindrome-number
# Title: 9. Palindrome Number
# Difficulty: Easy
# Topics: Math
# Likes: 13269, Dislikes: 2779
# Submitted: 9.6M, Accepted: 5.6M (58.0%)


question = """
Given an integer x, return true if x is a palindrome, and false otherwise.
 
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 
Constraints:

-2^31 <= x <= 2^31 - 1

 
Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        num_digits = len(x_str)
        for i in range(num_digits // 2):
            if x_str[i] != x_str[num_digits - i - 1]:
                return False
        return True


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        digits = []  # if the input number is 0, the list will be remain empty
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        num_digits = len(digits)
        for i in range(num_digits // 2):
            if digits[i] != digits[num_digits - i - 1]:
                return False
        return True
