# LeetCode 3: Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Store unique characters
        seen = set()

        # Left pointer
        left = 0

        # Maximum length found
        maxLength = 0