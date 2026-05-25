# ============================================================
# Day 10 Part 1 - Python DSA Practice
# Author : Chitralekha Ghadge
# Topics : Regular Expressions and File Handling
# ============================================================


# ============================================================
# 1. Introduction to Regular Expressions
# ============================================================

# Applications of Regular Expressions:
# 1. Digital Circuits
# 2. Compiler and Interpreter
# 3. Communication Protocols
# 4. Pattern Matching
# 5. Data Validation


# ============================================================
# 2. finditer() Example
# ============================================================

import re

print("1. finditer() Example\n")

count = 0

pattern = re.compile("function")

text = """
A function in Python is a reusable block of code that performs a specific task.
A function helps in reducing code repetition and makes the program more organized.
Whenever the same task needs to be performed multiple times, a function can be used.
"""

matcher = pattern.finditer(text)

for i in matcher:
    count += 1
    print(i.start(), "...", i.end(), "...", i.group())

print("The number of occurrences:", count)

print("\n" + "=" * 60)


# ============================================================
# 3. finditer() Simple Example
# ============================================================

print("\n2. finditer() with Simple String\n")

count = 0

matcher = re.finditer("hi", "hihihihi")

for i in matcher:
    count += 1
    print(i.start(), "...", i.end(), "...", i.group())

print("The number of occurrences:", count)

print("\n" + "=" * 60)


# ============================================================
# 4. match() Function
# ============================================================

print("\n3. match() Function\n")

a = "python"

mtch = re.match(a, "python is very important language")

if mtch is not None:
    print("Match found at beginning level")
    print(mtch.start(), mtch.end())
else:
    print("No match found")

print("\n" + "=" * 60)


# ============================================================
# 5. fullmatch() Function
# ============================================================

print("\n4. fullmatch() Function\n")

text = "python"

mtch = re.fullmatch(text, "python")

if mtch is not None:
    print("Full match found")
    print(mtch.start(), mtch.end())
else:
    print("Full match not found")

print("\n" + "=" * 60)


# ============================================================
# 6. Gmail Validation
# ============================================================

print("\n5. Gmail Validation\n")

email = "example@gmail.com"

m = re.fullmatch(r"\w[a-zA-Z0-9_.]*@gmail[.]com", email)

if m is not None:
    print("Valid Gmail ID")
else:
    print("Invalid Gmail ID")

print("\n" + "=" * 60)


# ============================================================
# 7. College Email Validation
# ============================================================

print("\n6. College Email Validation\n")

email = "student@rbunagpur.in"

m = re.fullmatch(r"\w[a-zA-Z0-9_.]*@rbunagpur[.]in", email)

if m is not None:
    print("Valid College Email ID")
else:
    print("Invalid College Email ID")

print("\n" + "=" * 60)


# ============================================================
# 8. Mobile Number Validation
# ============================================================

print("\n7. Mobile Number Validation\n")

mobile = "9876543210"

pattern = "^[6-9][0-9]{9}$"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

print("\n" + "=" * 60)


# ============================================================
# 9. search() Function
# ============================================================

print("\n8. search() Function\n")

mtch = re.search("dynamic", "python is a dynamic language")

if mtch is not None:
    print(mtch.start(), mtch.end(), mtch.group())
else:
    print("No matching found")

print("\n" + "=" * 60)


# ============================================================
# 10. findall() Function
# ============================================================

print("\n9. findall() Function\n")

mtch = re.findall('[A-Z]', "abch3hbhjsicfcfinnQWGYYWGQK")

print(mtch)

print("\n" + "=" * 60)


# ============================================================
# 11. sub() Function
# ============================================================

print("\n10. sub() Function\n")

obj = re.sub('[a-z]', '*', '2345 ABCD habc deff')

print(obj)

print("\n" + "=" * 60)


# ============================================================
# 12. subn() Function
# ============================================================

print("\n11. subn() Function\n")

obj = re.subn('[0-7]', '@', 'ab3gd6nkl7')

print("Modified String:", obj[0])
print("Number of Replacements:", obj[1])

print("\n" + "=" * 60)


# ============================================================
# 13. Extract Mobile Numbers from File
# ============================================================

print("\n12. Extract Mobile Numbers from File\n")

# Uncomment when input.txt exists

# f1 = open("input.txt", "r")
# f2 = open("output.txt", "w")

# data = f1.read()

# numbers = re.findall("[6-9][0-9]{9}", data)

# for i in numbers:
#     f2.write(i + "\n")

# print("Mobile numbers extracted successfully")

# f1.close()
# f2.close()

print("Code available for extracting mobile numbers")

print("\n" + "=" * 60)


# ============================================================
# 14. Extract Email IDs from File
# ============================================================

print("\n13. Extract Email IDs from File\n")

# Uncomment when input1.txt exists

# f1 = open("input1.txt", "r")
# data = f1.read()

# emails = re.findall(r'\S+@\S+', data)

# print("Email IDs are:")

# for i in emails:
#     print(i)

# f1.close()

print("Code available for extracting email IDs")

print("\n" + "=" * 60)


# ============================================================
# 15. Count Lines, Words and Characters in File
# ============================================================

print("\n14. Count Lines, Words and Characters\n")

import os
import sys

fname = input("Enter File Name: ")

if os.path.isfile(fname):

    print("File exists:", fname)

    f = open(fname, "r")

else:

    print("File does not exist:", fname)

    sys.exit(0)

lcount = 0
wcount = 0
ccount = 0

for line in f:

    lcount += 1

    ccount += len(line)

    words = line.split()

    wcount += len(words)

print("The number of lines:", lcount)
print("The number of words:", wcount)
print("The number of characters:", ccount)

f.close()

print("\n" + "=" * 60)


# ============================================================
# Summary
# ============================================================
# ✔ Regular Expressions
# ✔ finditer()
# ✔ match()
# ✔ fullmatch()
# ✔ search()
# ✔ findall()
# ✔ sub()
# ✔ subn()
# ✔ Email Validation
# ✔ Mobile Validation
# ✔ File Handling
# ✔ Extract Data from Files
# ============================================================

print("\nDay 10 Part 1 Practice Completed Successfully 🚀")