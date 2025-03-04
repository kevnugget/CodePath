# Prob 1

# Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

def cast_vote(votes, candidate):
    votes[candidate] = votes.get(candidate, 0) + 1

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

# Prob 2

# Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.
def common_keys(dict1, dict2):
   result = []
   for key in dict1:
       if key in dict2:
           result.append(key)
   return result

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

# Prob 3

# Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
# If two tasks have the same priority, return the task that comes first in the alphabet.

def get_highest_priority_task(tasks):
    highest_task = max(tasks, key = tasks.get)
    tasks.pop(highest_task)
    return highest_task

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)

# Problem 4

# Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.

def count_occurrences(nums):
    result = {}
    for num in nums:
        result[num] = result.get(num, 0) + 1
    return result

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))\

# Problem 5

d