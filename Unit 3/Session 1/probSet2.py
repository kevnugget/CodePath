# Problem 1
def match_made(dictionary):
	for key, value in dictionary.items():
		print( f"{key} and {value} are a perfect match.")
		
match = {"Peanut butter" : "jelly", "Spongebob" : "Patrick", "Ash" : "Pikachu"}
match_made(match)

# Problem 2

# Write a function that takes a string and removes the nth character, where 0 < n < len(s)
def remove_char(s, n):
	return s[0: n] + s[n + 1:]

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

# Problem 3

# Write a function that takes a string and returns the num of vowels
def vowel_count(s):
	num_vowel = 0
	for letter in s.lower():
		if letter.isalpha() and letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
			num_vowel += 1
	return num_vowel

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

# Problem 4

# Write a function reverse_sentence() that returns the string but with the order reversed
def reverse_sentence(sentence):
	words = sentence.split()
	return " ".join(words[::-1])

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))

# Problem 5

#Write a function that compresses the string to char and number of time it appears in a row
def compress_string(my_str):
	count = 1
	result = ""
	for i in range(len(my_str)-1):
		if my_str[i] == my_str[i+1]:
			count += 1
		else:
			result += my_str[i] + str(count)
			count = 0
	return result if len(result) < len(my_str) else my_str

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)