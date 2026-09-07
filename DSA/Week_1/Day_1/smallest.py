inp=[10,30,60,12,99,100]
sml=float("+inf")
for i in inp:
    if i < sml:
        sml=i
print("Smallest:",sml)

"""
    Find Smallest Element in Array
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using one variable
    
    Approach: Iterate through array, track minimum value
    """