# Find H.C.F. (G.C.D.) of two number 
def find_gcd(x, y): 
    while(y): 
        x, y = y, int(x % y) 
    return x 

def generalizedGCD(num, arr):
    if(1 in arr):
        return 1
    
    # GCD of more than two (or array) numbers greater than 1 
    gcd = arr[0]
    
    # s = "GCD for first 2 number " + str(arr[0]) + " and " + str(arr[1]) + " is " + str(gcd)
    # print s
    for i in range(0, len(arr)):
        if(gcd==1):
            return gcd
        
        # s = "GCD for " + str(gcd) + " and number at " + str(i) + " position " + str(arr[i]) + " is "
        if(arr[i]!=0):
            gcd = find_gcd(gcd, arr[i])
        
        # print s + str(gcd)
    return gcd