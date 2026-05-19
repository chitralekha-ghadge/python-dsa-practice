# ==========================================
# Day 7 Python Practice Problems - Part 1
# Author: Chitralekha Ghadge
# Topics: Recursion, Strings, Arrays
# ==========================================


# =========================================================
# 1. Find First Non-Repeating Character
# =========================================================
# Question:
# Write a function to find the first non-repeating
# character in a string.
#
# Logic:
# Count occurrences of every character and return
# the first character whose count is 1.
#
# Sample Input:
# "leetcode"
#
# Expected Output:
# "l"
# =========================================================

print("1. First Non-Repeating Character\n")


def first_non_repeating(s):

    for ch in s:

        count = 0

        # Count occurrences of character
        for c in s:

            if ch == c:
                count += 1

        # Character appears only once
        if count == 1:
            return ch

    # If no non-repeating character exists
    return None


# Sample Input
string = "leetcode"

# Function Call
result = first_non_repeating(string)

# Output
if result is not None:
    print("First non-repeating character is :", result)

else:
    print("No non-repeating character found")

print("\n" + "=" * 60 + "\n")


# =========================================================
# 2. Recursion Notes
# =========================================================
# Recursion:
# A function calling itself repeatedly.
#
# Important for:
# - Tree Traversal
# - DFS / BFS
# - Backtracking
# - Divide and Conquer
#
# Every recursive function requires:
# 1. Base Condition
# 2. Recursive Call
# =========================================================

print("2. Recursion Notes\n")

print("Recursion is important for interviews.")
print("Used in Trees, Graphs, DFS, BFS, etc.")

print("\n" + "=" * 60 + "\n")


# =========================================================
# 3. Factorial using Recursion
# =========================================================
# Formula:
# n! = n * (n-1)!
#
# Example:
# 5! = 5 * 4 * 3 * 2 * 1
# =========================================================

print("3. Factorial using Recursion\n")


def factorial(num):

    # Base Condition
    if num <= 1:
        return 1

    # Recursive Call
    return num * factorial(num - 1)


print("Factorial of 4 is :", factorial(4))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 4. Capitalize First Letter using Recursion
# =========================================================

print("4. Capitalize First Letter using Recursion\n")


def capitalizeFirst(arr):

    result = []

    # Base Condition
    if len(arr) == 0:
        return result

    # Capitalize first character
    result.append(
        arr[0][0].upper() + arr[0][1:]
    )

    # Recursive Call
    return result + capitalizeFirst(arr[1:])


print(
    capitalizeFirst(
        ['car', 'taco', 'banana']
    )
)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 5. Power Function using Recursion
# =========================================================
# Formula:
# base^exponent
# =========================================================

print("5. Power Function using Recursion\n")


def power(base, exponent):

    # Base Condition
    if exponent == 0:
        return 1

    # Recursive Call
    return base * power(base, exponent - 1)


print("2^0 =", power(2, 0))
print("2^2 =", power(2, 2))
print("2^4 =", power(2, 4))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 6. Product of Array using Recursion
# =========================================================

print("6. Product of Array using Recursion\n")


def productOfArray(arr):

    # Base Condition
    if len(arr) == 0:
        return 1

    # Recursive Call
    return arr[0] * productOfArray(arr[1:])


print(productOfArray([1, 2, 3]))
print(productOfArray([1, 2, 3, 10]))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 7. Reverse a String using Recursion
# =========================================================

print("7. Reverse a String using Recursion\n")


def reverse(string):

    # Base Condition
    if len(string) <= 1:
        return string

    # Recursive Call
    return string[-1] + reverse(string[:-1])


print(reverse('python'))
print(reverse('appmillers'))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 8. Recursive Range Solution
# =========================================================
# Sum of numbers from n to 1
# =========================================================

print("8. Recursive Range Solution\n")


def recursiveRange(num):

    # Base Condition
    if num <= 0:
        return 0

    # Recursive Call
    return num + recursiveRange(num - 1)


print("Sum is :", recursiveRange(6))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 9. Palindrome Check using Recursion
# =========================================================

print("9. Palindrome Check using Recursion\n")


def isPalindrome(string):

    # Base Condition
    if len(string) == 0 or len(string) == 1:
        return True

    # Check first and last character
    if string[0] != string[-1]:
        return False

    # Recursive Call
    return isPalindrome(string[1:-1])


word = "madam"

if isPalindrome(word):
    print(word, "is a Palindrome")

else:
    print(word, "is not a Palindrome")

print("\n" + "=" * 60 + "\n")


# =========================================================
# 10. someRecursive Solution
# =========================================================
# Check whether at least one element satisfies
# the given condition.
# =========================================================

print("10. someRecursive Solution\n")


def someRecursive(arr, condition):

    # Base Condition
    if len(arr) == 0:
        return False

    # Check condition
    if not condition(arr[0]):
        return someRecursive(arr[1:], condition)

    return True


# Function to check odd number
def isOdd(num):

    if num % 2 == 0:
        return False

    else:
        return True


# Test Cases
print(someRecursive([1, 2, 3, 4], isOdd))
print(someRecursive([4, 6, 8, 9], isOdd))
print(someRecursive([4, 6, 8], isOdd))

print("\n" + "=" * 60 + "\n")


# =========================================================
# Summary of Concepts Practiced
# =========================================================
# ✔ Strings
# ✔ Arrays
# ✔ Recursion
# ✔ Base Condition
# ✔ Recursive Calls
# ✔ Problem Solving
# ✔ Functions
# =========================================================

print("Day 7 Part 1 Practice Completed Successfully 🚀")