inp=[10,30,60,12,99,100]
ceven=0
codd=0
for num in inp:
    if num%2==0:
        ceven+=1
    else:
        codd+=1
print("Even : ",ceven,"Odd :",codd)

"""
    Count Even and Odd Numbers
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using two variables
    
    Approach: Iterate through array, check each number's parity
    """