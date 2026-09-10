class Solution(object):
    def topKFrequent(self, nums, k):
        mydict={}
        res=[]
        for num in nums:
            mydict[num]=mydict.get(num,0)+1
        llist=[]
        for i in range(len(nums)+1):
            llist.append([])
        for key,val in mydict.items():
            llist[val].append(key)
        for i in range(len(llist)-1,-1,-1):
            for n in llist[i]:
                res.append(n)
            if len(res)==k:
                return res
            


# LeetCode 347 - Top K Frequent Elements
# Pattern: HashMap + Bucket Sort
# Idea: Count frequency → Bucket index = frequency → Traverse from high to low.
# Time: O(n)
# Space: O(n)
# Learning: Use buckets to avoid O(n log n) sorting.