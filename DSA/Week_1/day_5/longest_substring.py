class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        maximum=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maximum=max(maximum,right-left+1)
        return maximum

            
# LeetCode 3 - Longest Substring Without Repeating Characters
# Pattern: Sliding Window + HashSet
# Idea: Expand right, shrink left when duplicate appears.
# Time: O(n)
# Space: O(n)