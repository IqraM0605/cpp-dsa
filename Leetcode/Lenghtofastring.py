class Solution:
    def lengthOfLongestSubstring(self, s):

        seen = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            maxLength = max(maxLength, right - left + 1)

        return maxLength


obj = Solution()

print(obj.lengthOfLongestSubstring("abcabcbb"))
print(obj.lengthOfLongestSubstring("bbbbb"))
print(obj.lengthOfLongestSubstring("pwwkew"))
print(obj.lengthOfLongestSubstring(""))
print(obj.lengthOfLongestSubstring("abba"))