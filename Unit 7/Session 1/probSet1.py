# Prob 1: Write a function that produces the same output without using recursion.
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)

def repeat_hello_iterative(n):
	for i in range(n):
		print('Hello')
		
repeat_hello_iterative(5)

# Prob 2: Write a function that returns the factorial of a non-negative integer.
def factorial(n):
	if n == 0:
		return 1
	else:
		return factorial(n - 1) * n
	
print(factorial(5))

# Prob 3: Write a function that sums all values in a list recursively
def sum_list(lst):
	if not lst:
		return 0
	else:
		return lst[0] + sum_list(lst[1:])
	
lst = [1,2,3,4,5]
print(sum_list(lst))

# Prob 4: Write a function that verifies if n is a power of 2.
def is_power_of_two(n):
	if n <= 0: # invalid case
		return False
	if n == 1: # Base case
		return True
	if n % 2 != 0: # n has to be divisible by 2
		return False
	else:
		return is_power_of_two(int(n / 2)) # O(log n)

print(is_power_of_two(6)) 

# Prob 5: Write an iterative implementation binary research.
def binary_search(lst, target):
	left = 0
	right = len(lst) - 1
	while left < right:
		mid = int((left + right) / 2) # O(log n), we are "dividing" the list in half everytime we compare target to mid
		if lst[mid] == target:
			return mid
		elif lst[mid] < target:
			left = mid
		else:
			right = mid
	return -1

lst = [1,3,5,7,9,11,13,15]
print(binary_search(lst, 11))

# Prob 6: Write an updated version of binary search, find_last(), that returns the last index of target
def find_last(lst, target):
	left = 0
	right = len(lst) - 1
	last_index = -1
	while left < right:
		mid = int((left + right) / 2) # O(log n), we are "dividing" the list in half everytime we compare target to mid
		if lst[mid] == target:
			last_index = mid
			left = mid + 1 # continue searching
		elif lst[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return last_index

lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
print(find_last(lst,11))

# Prob 7: Given a sorted list of integers and a value x, return the index of the floor of x.
def find_floor(lst, x):
	left = 0
	right = len(lst) - 1
	while left < right:
		mid_point = int((left + right)/2)
		if lst[mid_point] <= x: 
			return mid_point
		elif lst[mid_point] < x:
			left = mid_point
		else:
			right = mid_point
	return -1

lst = [1, 2, 8, 10, 11, 12, 19]
print(find_floor(lst, 5))
		
