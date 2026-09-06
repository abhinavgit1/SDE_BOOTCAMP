
inp=[10,30,60,12,99,100]
sr=int(input("Enter the number to be searched"))
res=-1
for i in range(0,len(inp)):
    if inp[i]==sr:
        res=i
        break
print(res)

"""
    Linear Search Algorithm
    Time Complexity: O(n) - worst case, we check all elements
    Space Complexity: O(1) - only using constant space
    
    Approach: Iterate through array and return index when element found
    Use Case: Small arrays or unsorted data
    """