# ==========================================
# Day 7 Python Practice Problems - Part 2
# Author: Chitralekha Ghadge
# Topics: Arrays, Trees, Linked List, Recursion
# ==========================================


# =========================================================
# 1. Maximum Product Pair Problem
# =========================================================
# Question:
# Find the sum of two cards whose product is maximum.
#
# Sample Input:
# [9, -3, 8, -6, -7, 8, 10]
#
# Expected Output:
# 19
# =========================================================

print("1. Maximum Product Pair Problem\n")

cards = [9, -3, 8, -6, -7, 8, 10]

max_product = float('-inf')
winning_sum = 0

# Check all possible pairs
for i in range(len(cards)):

    for j in range(i + 1, len(cards)):

        product = cards[i] * cards[j]

        if product > max_product:

            max_product = product
            winning_sum = cards[i] + cards[j]

print("Cards :", cards)
print("Maximum Product :", max_product)
print("Winning Sum :", winning_sum)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 2. Tree Representation using List
# =========================================================
# Tree is a nonlinear data structure.
#
# Terms:
# Root
# Edge
# Leaf
# Sibling
# Ancestor
# Height
# Depth
# =========================================================

print("2. Tree Representation using List\n")


class Tree:

    def __init__(self, data):

        self.data = data
        self.child = []

    # Add child node
    def addChild(self, obj):

        self.child.append(obj)

    # Display Tree
    def __str__(self, level=0):

        ret = "  " * level + str(self.data) + "\n"

        for ch in self.child:

            ret += ch.__str__(level + 1)

        return ret


# Create Nodes
rootNode = Tree("Drinks")

Hot = Tree("Hot")
Cold = Tree("Cold")

Tea = Tree("Tea")
Coffee = Tree("Coffee")

NonAlcoholic = Tree("NonAlcoholic")
Alcoholic = Tree("Alcoholic")

# Connect Nodes
rootNode.addChild(Hot)
rootNode.addChild(Cold)

Hot.addChild(Tea)
Hot.addChild(Coffee)

Cold.addChild(NonAlcoholic)
Cold.addChild(Alcoholic)

# Print Tree
print(rootNode)

print("=" * 60 + "\n")


# =========================================================
# 3. Another Tree Example
# =========================================================

print("3. Tree Example using Nodes\n")

rootNode = Tree("N1")

N2 = Tree("N2")
N3 = Tree("N3")
N4 = Tree("N4")
N5 = Tree("N5")
N6 = Tree("N6")
N7 = Tree("N7")
N8 = Tree("N8")

# Connect Nodes
rootNode.addChild(N2)
rootNode.addChild(N3)

N2.addChild(N4)
N2.addChild(N5)

N3.addChild(N6)

N4.addChild(N7)
N4.addChild(N8)

# Print Tree
print(rootNode)

print("=" * 60 + "\n")


# =========================================================
# 4. Time Complexity of Tree Operations
# =========================================================

print("4. Time Complexity of Tree Operations\n")

print("Creation                    -> O(1)")
print("Insertion                   -> O(n)")
print("Searching                   -> O(n)")
print("Traversing                  -> O(n)")
print("Deletion of Node            -> O(n)")
print("Deletion of Linked List     -> O(1)")

print("\n" + "=" * 60 + "\n")


# =========================================================
# 5. Insert Node at Tail of Linked List
# =========================================================
# HackerRank Problem
# =========================================================

print("5. Insert Node at Tail of Linked List\n")


class SinglyLinkedListNode:

    def __init__(self, node_data):

        self.data = node_data
        self.next = None


# Function to insert node at tail
def insertNodeAtTail(head, data):

    new_node = SinglyLinkedListNode(data)

    # If linked list empty
    if head is None:
        return new_node

    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.next = new_node

    return head


# Function to display linked list
def display(head):

    temp = head

    while temp is not None:

        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


# Driver Code
head = None

head = insertNodeAtTail(head, 10)
head = insertNodeAtTail(head, 20)
head = insertNodeAtTail(head, 30)

display(head)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 6. Sort Colors Problem
# =========================================================
# LeetCode Problem
#
# Sort array containing:
# 0 -> Red
# 1 -> White
# 2 -> Blue
# =========================================================

print("6. Sort Colors Problem\n")


def sortColors(nums):

    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:

            nums[low], nums[mid] = nums[mid], nums[low]

            low += 1
            mid += 1

        elif nums[mid] == 1:

            mid += 1

        else:

            nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1

    return nums


nums = [2, 0, 2, 1, 1, 0]

print("Original Array :", nums)
print("Sorted Colors  :", sortColors(nums))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 7. Insertion Sort - Part 1
# =========================================================
# HackerRank Problem
# =========================================================

print("7. Insertion Sort - Part 1\n")


def insertionSort1(n, arr):

    value = arr[n - 1]

    i = n - 2

    while i >= 0 and arr[i] > value:

        arr[i + 1] = arr[i]

        print(arr)

        i -= 1

    arr[i + 1] = value

    print(arr)


arr = [2, 4, 6, 8, 3]

print("Original Array :", arr)

insertionSort1(len(arr), arr)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 8. Recursive Digit Sum
# =========================================================
# HackerRank Problem
# =========================================================

print("8. Recursive Digit Sum\n")


def superDigit(n, k):

    # Sum of digits
    total = sum(int(digit) for digit in n) * k

    # Recursive Function
    def findSuperDigit(num):

        # Base Condition
        if num < 10:
            return num

        s = 0

        while num > 0:

            s += num % 10
            num //= 10

        return findSuperDigit(s)

    return findSuperDigit(total)


n = "148"
k = 3

print("Super Digit :", superDigit(n, k))

print("\n" + "=" * 60 + "\n")


# =========================================================
# 9. Array Rotation
# =========================================================
# Question:
# Rotate array to the right by k steps.
#
# Sample Input:
# [1, 2, 3, 4, 5]
#
# k = 2
#
# Expected Output:
# [4, 5, 1, 2, 3]
# =========================================================

print("9. Array Rotation\n")

arr = [1, 2, 3, 4, 5]

k = 2

# Rotate Array
rotated = arr[-k:] + arr[:-k]

print("Original Array :", arr)
print("Rotated Array  :", rotated)

print("\n" + "=" * 60 + "\n")


# =========================================================
# Summary of Concepts Practiced
# =========================================================
# ✔ Arrays
# ✔ Trees
# ✔ Linked List
# ✔ Recursion
# ✔ Sorting
# ✔ Time Complexity
# ✔ HackerRank Problems
# ✔ LeetCode Problems
# =========================================================

print("Day 7 Part 2 Practice Completed Successfully 🚀")