# Problem 1
def hello_world():
    print("Hello world!")
    
hello_world()

# Problem 2
def todays_mood():
    mood = '🥱'
    print("Today's mood: " + mood)
    
todays_mood()

# Problem 3
def print_menu(menu):
    print("Lunch today is: " + menu)
    
print_menu('🍜')

# Problem 4
def sum(a, b):
    return a + b

print(2 * sum(13, 27))

# Problem 5
def product(a, b):
    return a*b

print(product(22, 7))

# Problem 6
def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
    
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)
    
# Problem 7

def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12: 
        return "peanut butter jelly time 🥪"
    else: 
        return "nap time 😴"
    
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

# Problem 8

def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")
        
blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)

def get_first(lst):
    return lst[0]

# Problem 9
lst = [3, 1, 6, 7, 5]
print(get_first(lst))

# Problem 10

def get_last(lst):
    return lst[-1]

lst = [3, 1, 6, 7, 5]
print(get_last(lst))

# Problem 11

def counter(stop):
    for i in range(1, stop + 1):
        print(i)

counter(7)

# Problem 12

def sum_ten():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum

output = sum_ten()
print(output)

# Problem 13

def sum_positive_range(stop):
    sum = 0
    for i in range(1, stop + 1):
        sum += i
    return sum

sum = sum_positive_range(6)
print(sum)

# Problem 14

def sum_range(start, stop):
    sum = 0
    for i in range(start, stop + 1):
        sum += i
    return sum

sum = sum_range(3, 9)
print(sum)

# Problem 15

def print_negatives(lst):
    for number in lst:
        if number < 0:
            print(number)

print_negatives([3, -2, 2, 1, -5])