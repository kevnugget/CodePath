# Problem 1

# Call the function so that it prints out the following to the console (without calling the function more than once):
#1 mississipi
#2 mississipi
#3 mississipi
#4 mississipi
#5 mississipi
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

count_mississippi(6)

# Problem 2

# Write a functon, swap_ends(my_str) that swaps the first and last character
def swap_ends(my_str):
    result = my_str[-1] + my_str[1:-1] + my_str[0]
    return result

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

# Problem 3

# Write a function is_pangram(my_str) that returns true if it contains every letter in alphabet, false if it doesn't.
def is_pangram(my_str):
    seen_characters = set()
    for letter in my_str.lower():
        if letter.isalpha(): # accounts for spaces
            seen_characters.add(letter)
    return len(seen_characters) == 26

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

# Problem 4

# Write a function, reverse_string(my_str), that returns the string reversed
def reverse_string(my_str):
    return my_str[::-1]

print(reverse_string('boat'))

# Problem 5

# Write a function, first_unique_char(my_str), that returns the index of the first non-repeating character. If none, return -1
def first_unique_char(my_str):
    unique = {}
    for i in range(len(my_str)): # occurences of each character
        unique[my_str[i]] = unique.get(my_str[i], 0) + 1

    for index, char in enumerate(my_str): # enumerate(my_str) gives (index, character)
        if unique[char] == 1:
            return index
    return -1


my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

# Problem 6

# Write a function, min_distance(words, word1, word2) that returns the minimum distance of word1 and word2
def min_distance(words, word1, word2):
    word1_index, word2_index = -1, -1
    minimum = len(words)
    for index, word in enumerate(words):
        if word == word1: # find each word and its index
            word1_index = index
        if word == word2:
            word2_index = index

        if word1_index != -1 and word2_index != -1: # update minimum if both words were found 
            minimum = min(minimum, abs(word1_index - word2_index))
    return minimum if minimum != len(words) else -1
    
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

