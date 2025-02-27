# Practice Problem with Anagrams
def group_anagrams(words):
    result = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]
    return list(result.values())


words = ['ant', 'tan', 'bet', 'teb']
print(group_anagrams(words))

# Prob 1
def is_monotonic(nums):
    for i in range(len(nums - 1)):
        if not (nums[i] <= nums[i + 1]) or (nums[i] >= nums[i + 1]):
            return False
    return True

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))

# Prob 2
def student_directory(student_names):
    result = {}
    student_id = 1
    for name in student_names:
        result[name] = student_id
        student_id += 1
    return result

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))

# Prob 3
def get_description(info, keys):
    for key in keys:
	    print(info[key])
    
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "age", "occupation"]
get_description(info, keys)

# Prob 4
def sum_even_values(dictionary):
    sum = 0
    for value in dictionary.values():
        if value % 2 == 0:
            sum += value
    return sum

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))