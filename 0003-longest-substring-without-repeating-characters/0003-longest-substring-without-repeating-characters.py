class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}      # stores last index of each character
        left = 0            # left pointer of sliding window
        max_length = 0      # result
        
        for right in range(len(s)):
            char = s[right]
            
            # If character seen and inside current window
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            
            # Update last seen index
            last_seen[char] = right
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length