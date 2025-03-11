# Problem 1

# Write a function is_prime() that takes a positive integer, n, and returns true if it is a prime and false otherwise
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1): # sqrt(n) * sqrt(n) = n, so upper bound of for loop must be sqrt(n) + 1
        if n % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(2))

# Prob 2

# Write a function that reverses a list's elements IN-PLACE
def reverse_list(lst):
    start_index = 0
    end_index = -1
    while start_index != int(len(lst)/2): # O(n/2) -> O(n)
        temp = lst[start_index]
        lst[start_index] = lst[end_index]
        lst[end_index] = temp

        start_index+=1
        end_index-=1
    return lst

lst = [1, 2, 3, 4, 5, 6]
print(reverse_list(lst))

# Prob 3
# Then, evaluate the time and space of the following solution:

# def reverse_list(lst):
#     # Create a new reversed list
#     reversed_lst = lst[::-1] Time: O(n) since it has iterate through each element and copy them. Space: O(n) since it creates a new list
#     # Copy the elements back into the original list
#     for i in range(len(lst)): Time: O(n) as it iterates through every element of lst
#         lst[i] = reversed_lst[i] # No extra space is created.
# Overall: Time complexity: O(n). Space complexity: O(n)

# Prob 4

# Write a function that moves all even integers to the beginning of the list, followed by the odd integers.
def sort_list_by_parity(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] % 2 != 0 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
        elif nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
    return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_list_by_parity(nums))
print(sort_list_by_parity(nums2))

# Prob 5
# Write a function first_palindrome() that takes a list of words and returns the first palindromic string

def first_palindrome(words):
    for word in words:
        start = 0
        end = len(word) - 1
        while start < end:
            if word[start] != word[end]:
                break
            else:
                start += 1
                end -= 1
        if start == end:
            return word
    return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

# Prob 6
# Write a function that takes a sorted list of integers and removes all duplicates IN PLACE.

def remove_duplicates(nums):
    if not nums: 
        return 0
    i = 0 # pointer for the unique elements
    for j in range(1, len(nums)):
        if nums[j] != nums[i]: # if unique element
            i+= 1
            nums[i] = nums[j] # move it to the correct position
    del nums[i+ 1:]
    return i + 1

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list
        
