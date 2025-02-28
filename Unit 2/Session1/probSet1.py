# Prob 1
def is_subsequence(lst, sequence):
    index = 0
    for num in lst:
        if num == sequence[index] and index < len(sequence):
            index += 1
    return index == len(sequence)

lst = [5, 1, 22, 25, -1, 6, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

# Prob 2
def create_dictionary(keys, values):
    index = 0
    result = {}
    for key in keys:
        result[key] = values[index]
        index += 1
    return result

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))

# Prob 3
def print_pair(dictionary, target):
    found = False
    for key in dictionary:
        if key == target:
            print("Key: " + key + "\nValue: " + dictionary[key])
            found = True
    if not found: 
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

# Prob 4
def keys_v_values(dictionary):
    keySum = valueSum = 0
    for key, value in dictionary.items():
        keySum += key
        valueSum += value
    if keySum > valueSum:
        return "keys"
    elif valueSum > keySum:
        return "values"
    else:
        return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

# Prob 5
def restock_inventory(current_inventory, restock_list):
    for key, value in restock_list.items():
        current_inventory[key] = current_inventory.get(key, 0) + value
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))

# Prob 6
def calculate_gpa(report_card):
    gpa = 0
    for value in report_card.values():
        if value == 'A':
            gpa += 4
        elif value =='B':
            gpa += 3
        elif value == 'C':
            gpa += 2
        elif value == 'D':
            gpa += 1
        elif value == 'F':
            gpa += 0
    return gpa/len(report_card.keys())

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

# Prob 7
def highest_rated(books):
    return max(books, key= lambda book: book['rating'])

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
print(highest_rated(books))

# Prob 8
def index_to_value_map(lst):
    index = 0
    result = {}
    for item in lst:
        result[index] = item
        index += 1
    return result

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))
