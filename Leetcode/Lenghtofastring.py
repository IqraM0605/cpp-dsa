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


# -----------------------
# Test Cases
# -----------------------

obj = Solution()

print("Input: abcabcbb")
print("Output:", obj.lengthOfLongestSubstring("abcabcbb"))

print()

print("Input: bbbbb")
print("Output:", obj.lengthOfLongestSubstring("bbbbb"))

print()

print("Input: pwwkew")
print("Output:", obj.lengthOfLongestSubstring("pwwkew"))

print()

print("Input: ''")
print("Output:", obj.lengthOfLongestSubstring(""))

print()

print("Input: abba")
print("Output:", obj.lengthOfLongestSubstring("abba"))