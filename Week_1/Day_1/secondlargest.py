def sc(inp):
    lar=float("-inf")
    slar=float("-inf")
    if len(inp)<2:
        return None
    for num in inp:
        if num>lar:
            slar=lar
            lar=num
        elif num>slar and num!=lar:
            slar=num
    print("Slargest : ",slar)
inp=[-10,-8,-5]
sc(inp)

"""
    Find Second Largest Element in Array (Optimized One-Pass)
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using two variables
    
    Approach: Track both largest and second largest simultaneously
    When larger element found: shift largest to second largest
    This is optimal - no sorting, no extra space, one pass!
    """
