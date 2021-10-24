'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
def firstMissingPositive(arr, n):
	ptr = 0
	for i in range(n):
		if arr[i] == 1:
			ptr = 1
			break
	if ptr == 0:
		return(1)
	for i in range(n):
		if arr[i] <= 0 or arr[i] > n:
			arr[i] = 1
	for i in range(n):
		arr[(arr[i] - 1) % n] += n
	for i in range(n):
		if arr[i] <= n:
			return(i + 1)
	return(n + 1)

A = [3, 4, -1, 1]
N = len(A)
print(firstMissingPositive(A, N))
