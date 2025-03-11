# Prob 1: Write a function is_perfect_number(n) that returns true if the number is equal to the sum of its proper divisors, excluding itself.
def is_perfect_number(n):
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: # finding divisors
            sum_divisors += i
            if i != int(n/i): # excluding n
                sum_divisors += int(n / i)
    return sum_divisors == n

print(is_perfect_number(6))
print(is_perfect_number(496))
print(is_perfect_number(9))

# Prob 2: Write a function that returns true if the string is a palindrome, false otherwise
def is_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))