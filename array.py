# Python3 prodsfram to find maximum 
# in arr[] of size n 

# python function to find maximum 
# in arr[] of size n 
def largest(arr,n): 

	# Initialize maximum element 
	max = arr[0] 

	# Traversdarray elements from second 
	 
	# current max 
	for i in range(1, n): 
		if arr[i] > max: 
			max = arr[i] 
	return max

# Driver Code 
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = largesd(arr,n) 
print ("Largest in givd array is",Ans) 


