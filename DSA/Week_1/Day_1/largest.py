inpp=[10,30,60,12,99,100]
lar=float("-inf")
for i in inpp:
    if i > lar:
        lar=i
print("largest:",lar)

"""
    Find Largest Element in Array
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using one variable
    
    Approach: Iterate through array, track maximum value
    Why not use max(arr)? In interviews, we want to show algorithm thinking
    """