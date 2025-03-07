# Problem 1

# Write a function sum_of_number_strings() that takes a list of strings that represents and integer and returns the sum of the integers.
def sum_of_number_strings(nums):
    sum = 0
    for number in nums:
        sum += int(number)
    return sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

# Problem 2

# Write a function that removes all duplicates from a sorted list of integers
def remove_duplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            nums.pop(nums[i + 1])
        else:
            i+=1
    return nums

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))

# Problem 3

# Write a function that takes in a string and reverses the order of only the letters
def reverse_only_letters(s):
    reversed_str = list(s)
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start].isalpha() and s[end].isalpha():
            reversed_str[start], reversed_str[end] = reversed_str[end], reversed_str[start]
            start += 1
            end -= 1
        elif not s[start].isalpha():
            start += 1
        elif not s[end].isalpha():
            end -= 1
    return ''.join(reversed_str)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# Problem 4

# Write a function that returns the length of the longest substring that contains the same singular character
def longest_uniform_substring(s):
    max_occurences = 1
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
        else:
            max_occurences = max(max_occurences, count)
    return max_occurences

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

# Problem 5

#  Write a function find_poisoned_duration() that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) and time_duration (the duration of the poisoning effect). The function returns the total time that Ashe is in a poisoned condition.
def find_poisoned_duration(time_series, duration):
    total_poison_time = 0
    for i in range(len(time_series) - 1):
        if time_series[i + 1] - time_series[i] < duration: # if the gap between current attack and next attack is less than duration, add the duration of the gap between them
            total_poison_time += time_series[i + 1] - time_series[i] - 1
        elif time_series[i+1] - time_series[i] > duration: # if the gap of current and next attack is greater than the duration, add the duration
            total_poison_time += duration
        else:
            total_poison_time += duration - 1 # if gap is exactly equal to duration, add the gap between the attacks
    total_poison_time += duration # account for last strike
    return total_poison_time

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)