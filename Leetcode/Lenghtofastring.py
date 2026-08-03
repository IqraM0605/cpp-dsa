# LeetCode 3: Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Store unique characters
        seen = set()

        # Left pointer
        left = 0

        # Maximum length found
        maxLength = 0
        print("Input: dvdf")
print("Output:", obj.lengthOfLongestSubstring("dvdf"))

print()

print("Input: anviaj")
print("Output:", obj.lengthOfLongestSubstring("anviaj"))
print(f'Input: "abcabcbb"')
print(f'Longest Length: {obj.lengthOfLongestSubstring("abcabcbb")}')
print("-" * 30)
def main():
    obj = Solution()

    print(obj.lengthOfLongestSubstring("abcabcbb"))
    print(obj.lengthOfLongestSubstring("bbbbb"))
    print(obj.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()
    # Time Complexity: O(n)
# Space Complexity: O(min(n, unique characters))