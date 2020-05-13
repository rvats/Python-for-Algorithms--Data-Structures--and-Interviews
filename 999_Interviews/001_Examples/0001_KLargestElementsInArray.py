# Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order. For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
def kLargest(arr, k): 
    # Sort the given array arr in reverse  
    # order. 
    arr.sort(reverse = True) 
    # Print the first kth largest elements 
    for i in range(k): 
        print (arr[i], end =" ")  
  
# Driver program 
arr = [1, 23, 12, 9, 30, 2, 50] 
# n = len(arr) 
k = 3
kLargest(arr, k) 
  