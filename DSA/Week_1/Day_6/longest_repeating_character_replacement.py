class Solution(object):
    def characterReplacement(self, s, k):
        i=0
        maxfreq=0
        mydict={}
        longest=0
        for right in range(len(s)):
            mydict[s[right]]=mydict.get(s[right],0)+1
            maxfreq=max(maxfreq,mydict.get(s[right]))
            while (right-i+1)-maxfreq > k:
                mydict[s[i]] -= 1
                i+=1
            longest=max(longest,right-i+1)
        return longest


# LeetCode 424 - Longest Repeating Character Replacement
# Pattern: Sliding Window + Frequency
# Idea: Expand right, shrink while (window - maxFreq) > k.
# Time: O(n)
# Space: O(1)