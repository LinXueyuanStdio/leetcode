'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.


Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
  s.length will be between 1 and 50,000.
  s will only consist of "0" or "1" characters.
'''
class Solution(object):
    def countBinarySubstrings(self, s):
        chunks, consecutive, res = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                consecutive += 1
            else:
                chunks.append(consecutive)
                consecutive = 1
        chunks.append(consecutive)
        for i in range(1, len(chunks)):
            res += min(chunks[i], chunks[i - 1])
        return res
        
class Solution(object):
    def countBinarySubstrings(self, s):
        flips, res = [0], 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                flips.append(i)
        flips.append(len(s))
        chunks = [a - b for (a, b) in zip(flips[1:], flips)]
        for i in range(1, len(chunks)):
            res += min(chunks[i], chunks[i - 1])
        return res
        
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        flips = [0] + [i for i in range(1, len(s)) if s[i] != s[i - 1]] + [len(s)]
        chunks = [a - b for (a, b) in zip(flips[1:], flips)]
        return sum(min(a, b) for a, b in zip(chunks, chunks[1:]))
