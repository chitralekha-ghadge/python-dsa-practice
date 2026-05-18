# ==========================================
# Day 6 Python Practice Problems - Part 1
# Author: Chitralekha Ghadge
# Topics: Strings, Stack, Sorting Algorithms
# ==========================================


# =========================================================
# 1. Reverse Each Word in a String
# =========================================================
# Question:
# Write a program to reverse each word in a string.
#
# Logic:
# Split the string into words, reverse each word,
# and join them back together.
#
# Sample Input:
# "Hello World"
#
# Expected Output:
# "olleH dlroW"
# =========================================================

print("1. Reverse Each Word in a String\n")

s = "Hello World"

# Split string into words
words = s.split()

# Reverse each word using slicing
reversed_words = [word[::-1] for word in words]

# Join reversed words back into string
result = " ".join(reversed_words)

print("Original String :", s)
print("Reversed String :", result)

# Alternative Method using loop
print("\nAlternative Method:")

result2 = ""

for word in words:
    result2 += word[::-1] + " "

print("Output :", result2.strip())

print("\n" + "=" * 60 + "\n")


# =========================================================
# 2. Check for Valid Parentheses
# =========================================================
# Question:
# Write a program to check if a string containing
# parentheses is valid.
#
# Logic:
# Use stack to track opening and closing brackets.
#
# Sample Input:
# "({[()]})"
#
# Expected Output:
# Valid
# =========================================================

print("2. Check for Valid Parentheses\n")


def is_valid(s):

    stack = []

    # Dictionary for matching brackets
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:

        # Push opening brackets into stack
        if char in "({[":
            stack.append(char)

        # Check closing brackets
        elif char in ")}]":

            # If stack is empty or mismatch occurs
            if not stack or stack[-1] != pairs[char]:
                return "Invalid"

            # Remove matched opening bracket
            stack.pop()

    # Stack should be empty for valid expression
    return "Valid" if not stack else "Invalid"


# Sample Input
s = "({[()]})"

print("Input  :", s)
print("Output :", is_valid(s))

# Additional Test Cases
print("\nExtra Test Cases:")
print("()[]{}       ->", is_valid("()[]{}"))
print("([)]         ->", is_valid("([)]"))
print("((()))       ->", is_valid("((()))"))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 3. Insertion Sort
# =========================================================
# Question:
# Sort an array using Insertion Sort.
#
# Logic:
# Compare current element with previous elements
# and place it at the correct position.
#
# Time Complexity:
# O(n²)
# =========================================================

print("3. Insertion Sort\n")

arr = [5, 3, 8, 6, 2]

print("Original Array :", arr)

# Insertion Sort Logic
for i in range(1, len(arr)):

    key = arr[i]
    j = i - 1

    # Shift elements greater than key
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # Insert key at correct position
    arr[j + 1] = key

print("Sorted Array   :", arr)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 4. Selection Sort
# =========================================================
# Question:
# Sort an array using Selection Sort.
#
# Logic:
# Find minimum element and swap with current index.
#
# Time Complexity:
# O(n²)
# =========================================================

print("4. Selection Sort\n")

arr = [20, 12, 10, 15, 2]

print("Original Array :", arr)

for i in range(len(arr)):

    # Assume current index as minimum
    min_index = i

    # Find actual minimum element
    for j in range(i + 1, len(arr)):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap elements
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array   :", arr)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 5. Built-in Sorting Method
# =========================================================
# Question:
# Sort a list using Python built-in sorted() function.
# =========================================================

print("5. Built-in Sorting Method\n")

numbers = [9, 4, 7, 1, 5]

print("Original List :", numbers)

# Using Python built-in sorted() method
sorted_numbers = sorted(numbers)

print("Sorted List   :", sorted_numbers)

print("\n" + "=" * 60 + "\n")


# =========================================================
# Summary of Concepts Practiced
# =========================================================
# ✔ String Manipulation
# ✔ List Comprehension
# ✔ Stack Implementation
# ✔ Sorting Algorithms
# ✔ Loops and Conditions
# ✔ Functions
# ✔ Time Complexity Basics
# =========================================================

print("Day 6 Part 1 Practice Completed Successfully 🚀")