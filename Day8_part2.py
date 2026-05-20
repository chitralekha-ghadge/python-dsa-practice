# ==========================================
# Day 8 Python Practice Problems - Part 2
# Author: Chitralekha Ghadge
# Topics: Linked List, Arrays, Backtracking,
# Error Handling, Logging, File Handling
# ==========================================


# =========================================================
# 1. Print Elements of Linked List
# =========================================================
# HackerRank Problem
#
# Print all elements of a singly linked list.
# =========================================================

print("1. Print Elements of Linked List\n")


class SinglyLinkedListNode:

    def __init__(self, node_data):

        self.data = node_data
        self.next = None


class SinglyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    # Insert Node
    def insert_node(self, node_data):

        node = SinglyLinkedListNode(node_data)

        # First node
        if not self.head:

            self.head = node

        else:

            self.tail.next = node

        self.tail = node


# Print Linked List
def printLinkedList(head):

    current = head

    while current is not None:

        print(current.data)

        current = current.next


# Driver Code
llist = SinglyLinkedList()

llist.insert_node(10)
llist.insert_node(20)
llist.insert_node(30)

print("Linked List Elements :")

printLinkedList(llist.head)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 2. Left Rotation of Array
# =========================================================
# HackerRank Problem
#
# Rotate array left by d positions.
# =========================================================

print("2. Left Rotation of Array\n")


def rotateLeft(d, arr):

    return arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5]

d = 2

print("Original Array :", arr)

print("Rotated Array  :", rotateLeft(d, arr))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 3. Best Time to Buy and Sell Stock
# =========================================================
# LeetCode Problem
# =========================================================

print("3. Best Time to Buy and Sell Stock\n")


def maxProfit(prices):

    min_price = float('inf')

    max_profit = 0

    for price in prices:

        # Minimum buying price
        if price < min_price:

            min_price = price

        # Profit calculation
        profit = price - min_price

        # Update max profit
        if profit > max_profit:

            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print("Prices :", prices)

print("Maximum Profit :", maxProfit(prices))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 4. Palindrome Number
# =========================================================
# LeetCode Problem
# =========================================================

print("4. Palindrome Number\n")


def isPalindrome(x):

    # Negative numbers are not palindrome
    if x < 0:

        return False

    original = x
    reverse = 0

    while x > 0:

        digit = x % 10

        reverse = reverse * 10 + digit

        x = x // 10

    return original == reverse


num = 121

print("Number :", num)

print("Is Palindrome :", isPalindrome(num))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 5. Permutations
# =========================================================
# LeetCode Problem
# Backtracking
# =========================================================

print("5. Permutations using Backtracking\n")


def permute(nums):

    result = []

    def backtrack(path, remaining):

        # Base Condition
        if len(remaining) == 0:

            result.append(path)

            return

        # Try every element
        for i in range(len(remaining)):

            current = remaining[i]

            new_remaining = (
                remaining[:i] +
                remaining[i + 1:]
            )

            backtrack(
                path + [current],
                new_remaining
            )

    backtrack([], nums)

    return result


nums = [1, 2, 3]

print("Input :", nums)

print("Permutations :")

print(permute(nums))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 6. Combination Sum
# =========================================================
# LeetCode Problem
# =========================================================

print("6. Combination Sum\n")


def combinationSum(candidates, target):

    result = []

    def backtrack(start, path, target):

        # Found valid combination
        if target == 0:

            result.append(path)

            return

        # Invalid path
        if target < 0:

            return

        # Try all candidates
        for i in range(start, len(candidates)):

            current = candidates[i]

            backtrack(
                i,
                path + [current],
                target - current
            )

    backtrack(0, [], target)

    return result


candidates = [2, 3, 6, 7]

target = 7

print("Candidates :", candidates)

print("Target :", target)

print("Combinations :")

print(combinationSum(candidates, target))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 7. Types of Errors
# =========================================================
# Runtime Error
# Compile Time Error
# =========================================================

print("7. Exception Handling\n")

try:

    a = int(input("Enter First Number : "))

    b = int(input("Enter Second Number : "))

    print("Division :", a / b)

except ZeroDivisionError:

    print("Cannot divide by zero")

except ValueError:

    print("Enter only integer values")

except Exception as message:

    print("Error :", message)

else:

    print("Everything is OK")

finally:

    print("Program execution completed")

print("\n" + "=" * 60 + "\n")


# =========================================================
# 8. Logging in Python
# =========================================================
# Logging Levels:
#
# CRITICAL -> 50
# ERROR    -> 40
# WARNING  -> 30
# INFO     -> 20
# DEBUG    -> 10
# NOTSET   -> 0
# =========================================================

print("8. Logging Example\n")

import logging

logging.basicConfig(
    filename="newfile.txt",
    level=logging.DEBUG
)

try:

    a = int(input("Enter First Integer : "))

    b = int(input("Enter Second Integer : "))

    print(a / b)

except (ZeroDivisionError, ValueError) as message:

    print(message)

    logging.exception(message)

print(
    "Logging setup completed."
)

print(
    "Check 'newfile.txt' for logs."
)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 9. CSV File Handling - Employee Record
# =========================================================
# Why use File Handling?
#
# To store permanent data in files.
# =========================================================

print("9. Employee CSV File Handling\n")

import csv

# Open CSV File
f = open(
    "employee.csv",
    'a',
    newline=''
)

a = csv.writer(f)

# Uncomment first time only
# a.writerow(["EmpID", "EmpName", "EmpAge"])

empid = int(input("Enter Employee ID : "))

empname = input("Enter Employee Name : ")

empage = int(input("Enter Employee Age : "))

# Write Data
a.writerow([empid, empname, empage])

print(
    "Employee record added successfully"
)

f.close()

print("\n" + "=" * 60 + "\n")


# =========================================================
# 10. Student Result CSV Project
# =========================================================
# Columns:
# studentId
# studentName
# phy
# chem
# math
# Total
# Percentage
# Result
# =========================================================

print("10. Student Result CSV Project\n")

f = open(
    "student.csv",
    'a',
    newline=''
)

a = csv.writer(f)

# Uncomment first time only
# a.writerow([
#     "studentId",
#     "studentName",
#     "phy",
#     "chem",
#     "math",
#     "Total",
#     "Percentage",
#     "Result"
# ])

studentId = int(
    input("Enter Student ID : ")
)

studentName = input(
    "Enter Student Name : "
)

phy = int(
    input("Enter Physics Marks : ")
)

chem = int(
    input("Enter Chemistry Marks : ")
)

math = int(
    input("Enter Maths Marks : ")
)

# Total Calculation
total = phy + chem + math

# Percentage Calculation
percentage = total / 3

# Result Logic
if (
    phy >= 40 and
    chem >= 40 and
    math >= 40
):

    result = "Pass"

else:

    result = "Fail"

# Write Data into CSV
a.writerow([
    studentId,
    studentName,
    phy,
    chem,
    math,
    total,
    percentage,
    result
])

print(
    "Student record added successfully"
)

f.close()

print("\n" + "=" * 60 + "\n")


# =========================================================
# Summary of Concepts Practiced
# =========================================================
# ✔ Linked List
# ✔ Arrays
# ✔ Backtracking
# ✔ Exception Handling
# ✔ Logging
# ✔ File Handling
# ✔ CSV Operations
# ✔ HackerRank Problems
# ✔ LeetCode Problems
# =========================================================

print("Day 8 Part 2 Practice Completed Successfully 🚀")