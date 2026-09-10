class Solution(object):
    def longestConsecutive(self, nums):
        length=0
        top=0
        sset=set(nums)
        for i in sset:
            if i-1 not in sset:
                length=1
                while i+length in sset:
                    length+=1
            if top<length:
                top=length
        return top
    
# LeetCode 128 - Longest Consecutive Sequence
# Pattern: HashSet (Sequence Detection)
# Idea: Start only when previous number doesn't exist, then expand forward.
# Time: O(n)
# Space: O(n)
# Learning: HashSet removes the need for sorting.