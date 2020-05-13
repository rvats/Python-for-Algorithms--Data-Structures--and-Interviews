# Pythagorean Triplet in an arrayGiven an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2. 
# Function to check if the Pythagorean triplet exists or not 
import math 
  
def checkTriplet(arr, n): 
    maximum = 0
  
    # Find the maximum element 
    for i in range(n): 
        maximum = max(maximum, arr[i]) 
  
        # Hashing array 
    hash = [0]*(maximum+1) 
  
    # Increase the count of array elements 
    # in hash table 
    for i in range(n): 
        hash[arr[i]] += 1
  
        # Iterate for all possible a 
    for i in range(1, maximum+1): 
        # If a is not there 
        if (hash[i] == 0): 
            continue
  
        # Iterate for all possible b 
        for j in range(1, maximum+1): 
            # If a and b are same and there is only one a 
            # or if there is no b in original array 
            if ((i == j and hash[i] == 1) or hash[j] == 0): 
                continue
  
            # Find c 
            val = int(math.sqrt(i * i + j * j)) 
  
            # If c^2 is not a perfect square 
            if ((val * val) != (i * i + j * j)): 
                continue
  
            # If c exceeds the maximum value 
            if (val > maximum): 
                continue
  
            # If there exists c in the original array, 
            # we have the triplet 
            if (hash[val]): 
                return True
    return False
  
  
# Driver Code 
arr = [3, 2, 4, 6, 5] 
n = len(arr) 
if (checkTriplet(arr, n)): 
    print("Yes") 
else: 
    print("No")