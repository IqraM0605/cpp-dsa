"""
LeetCode 3: Longest Substring Without Repeating Characters

Approach:
- Use a sliding window.
- Store unique characters in a set.
- If a duplicate appears, remove characters from the left
  until the duplicate is gone.
- Keep track of the maximum window size.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Stores unique characters in current window
        seen = set()

        # Left pointer of window
        left = 0

        # Stores answer
        maxLength = 0

        # Right pointer moves through the string
        for right in range(len(s)):

            # If duplicate found, shrink window
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character
            seen.add(s[right])

            # Update longest length
            maxLength = max(maxLength, right - left + 1)

        return maxLength


# -----------------------------
# Testing (Only for VS Code)
# -----------------------------
if __name__ == "__main__":

    obj = Solution()

    testCases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "abba",
        "dvdf",
        "anviaj"
    ]

    for s in testCases:
        print(f'Input : "{s}"')
        print(f'Output: {obj.lengthOfLongestSubstring(s)}')
        print("-" * 35)