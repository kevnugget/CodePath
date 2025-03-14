# Write a function that returns true if n is a perfect number, false otherwise.
#6 = (1, 2, 3) and 1 + 2 + 3 = 6
def is_perfect_number(n):
    divisor_sum = 0
    for i in range(1, n - 1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))

# Write a function that turns a string, s, into a palindrome with the minimum number of operations
def make_palindrome(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right] and s[left] < s[right]:
            s[right] = s[left]
        elif s[left] != s[right] and s[left] > s[right]:
            s[left] = s[right]
        else:
            left += 1
            right -= 1
    return "".join(s)

s = "egcfe"
s_pal = make_palindrome(s)
print(s_pal)

# Write a function that returns a string with all the vowels reversed
def reverse_vowel(s):
    s = list(s.lower())
    vowels = ['a', 'e', 'i', 'o', 'u']
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels:
            left += 1
        elif s[right] not in vowels: 
            right -= 1
    return "".join(s)

s1 = "hello"
rev_s1 = reverse_vowel(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowel(s2)
print(rev_s2)

# Write a function that takes a list nums and removes all instances of that value in-place
def remove_element(nums, val):
    i = 0
    for num in nums:
        if num != val:
            nums[i] = num
            i += 1
    del nums[i:]
    return len(nums)

nums = [5, 4, 4, 3, 4, 1]
nums_len = remove_element(nums, 4)
print(nums) # same list
print(nums_len)
