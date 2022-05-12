# Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        chars = set()
        l = 0
        r = 0
        while(l < len(s)-ans and r < len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                ans = max(ans, (r-l))
            else:
                chars.remove(s[l])
                l += 1
        return ans
