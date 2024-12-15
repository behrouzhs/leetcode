# URL: https://leetcode.com/problems/valid-parentheses
# Title: 20. Valid Parentheses
# Difficulty: Easy
# Topics: String, Stack
# Likes: 24843, Dislikes: 1831
# Submitted: 13M, Accepted: 5.4M (41.4%)


question = """
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

 
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

 
Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pass
