# Python3 program for the above approach
def Solution(arr):

	n = len(arr)

	z = n // 2
	# If length of array is even
	return (arr[z] + arr[z - 1]) / 2 if n % 2 == 0 else arr[z]

# Driver code
if __name__ == "__main__":

	arr1 = [ -5, 3, 6, 12, 15 ]
	arr2 = [ -12, -10, -6, -3, 4, 10 ]

	# Concatenating the two arrays
	arr3 = arr1 + arr2

	# Sorting the resultant array
	arr3.sort()

	print("Median = ", Solution(arr3))
	
# This code is contributed by kush11
