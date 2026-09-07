
def twoSum(nums,target):
    mydict={}
    for i,num in enumerate(nums):
        find=target-num
        if find in mydict:
            res=[i,mydict.get(find)]
            return res
        mydict[nums[i]]=i

print(twoSum([1,2,4,5,6],7))
