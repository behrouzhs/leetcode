# URL: https://leetcode.com/problems/longest-common-prefix
# Title: 14. Longest Common Prefix
# Difficulty: Easy
# Topics: String, Trie
# Likes: 18345, Dislikes: 4645
# Submitted: 9M, Accepted: 4M (44.3%)


question = """
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        
        common_prefix = list()
        for i, ch in enumerate(strs[0]):
            mismatch_found = False
            for string in strs[1:]:
                if i >= len(string) or string[i] != ch:
                    mismatch_found = True
                    break
            if mismatch_found:
                break
            common_prefix.append(ch)
        return ''.join(common_prefix)
