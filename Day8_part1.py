# ==========================================
# Day 8 Python Practice Problems - Part 1
# Author: Chitralekha Ghadge
# Topics: Arrays, Binary Tree, BST
# ==========================================


# =========================================================
# 1. Remove Leading Zeros from List
# =========================================================
# Question:
# Remove leading zeros from a list of integers.
#
# Sample Input:
# [0, 0, 1, 2, 0, 3, 0, 0, 4]
#
# Expected Output:
# [1, 2, 0, 3, 0, 0, 4]
# =========================================================

print("1. Remove Leading Zeros from List\n")


def remove_leading_zeros(lst):

    i = 0

    # Move index until non-zero element found
    while i < len(lst) and lst[i] == 0:

        i += 1

    return lst[i:]


numbers = [0, 0, 1, 2, 0, 3, 0, 0, 4]

print("Original List :", numbers)

result = remove_leading_zeros(numbers)

print("Updated List  :", result)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 2. First Missing Positive Integer
# =========================================================
# Question:
# Find the first missing positive integer.
#
# Sample Input:
# [3, 4, -1, 1]
#
# Expected Output:
# 2
# =========================================================

print("2. First Missing Positive Integer\n")


def first_missing_positive(arr):

    n = len(arr)

    # Place elements at correct index
    for i in range(n):

        while (
            1 <= arr[i] <= n and
            arr[arr[i] - 1] != arr[i]
        ):

            arr[arr[i] - 1], arr[i] = (
                arr[i],
                arr[arr[i] - 1]
            )

    # Find missing positive integer
    for i in range(n):

        if arr[i] != i + 1:
            return i + 1

    return n + 1


nums = [3, 4, -1, 1]

print("Input :", nums)

print(
    "First Missing Positive Integer :",
    first_missing_positive(nums)
)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 3. Smallest Missing Positive Integer
# =========================================================
# Question:
# Find the smallest missing positive integer.
#
# Sample Input:
# [7, 8, 9, 11, 12]
#
# Expected Output:
# 1
# =========================================================

print("3. Smallest Missing Positive Integer\n")


def smallest_missing_positive(arr):

    n = len(arr)

    # Rearrange elements
    for i in range(n):

        while (
            1 <= arr[i] <= n and
            arr[arr[i] - 1] != arr[i]
        ):

            arr[arr[i] - 1], arr[i] = (
                arr[i],
                arr[arr[i] - 1]
            )

    # Find missing number
    for i in range(n):

        if arr[i] != i + 1:
            return i + 1

    return n + 1


nums = [7, 8, 9, 11, 12]

print("Input :", nums)

print(
    "Smallest Missing Positive Integer :",
    smallest_missing_positive(nums)
)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 4. Binary Tree Notes
# =========================================================
# Types of Binary Tree:
#
# 1. Full Binary Tree
# 2. Complete Binary Tree
# 3. Perfect Binary Tree
# 4. Balanced Binary Tree
# =========================================================

print("4. Binary Tree Notes\n")

print("1. Full Binary Tree")
print("Each node has either 0 or 2 children\n")

print("2. Complete Binary Tree")
print("All levels are completely filled")
print("except possibly the last level\n")

print("3. Perfect Binary Tree")
print("All internal nodes have exactly")
print("two children and leaf nodes")
print("are at same level\n")

print("4. Balanced Binary Tree")
print("Height difference between left")
print("and right subtree is minimal")

print("\n" + "=" * 60 + "\n")


# =========================================================
# 5. Binary Search Tree (BST)
# =========================================================
# BST performs faster searching,
# insertion and deletion than normal tree.
# =========================================================

print("5. Binary Search Tree Implementation\n")


# =========================================================
# BST Node Class
# =========================================================

class BSTNode:

    def __init__(self, data):

        self.data = data
        self.leftChild = None
        self.rightChild = None


# =========================================================
# Insert Node Function
# =========================================================

def insertNode(rootNode, nodeValue):

    # Insert root node
    if rootNode.data is None:

        rootNode.data = nodeValue
        return

    # Insert left side
    elif nodeValue <= rootNode.data:

        if rootNode.leftChild is None:

            rootNode.leftChild = BSTNode(nodeValue)

        else:

            insertNode(
                rootNode.leftChild,
                nodeValue
            )

    # Insert right side
    else:

        if rootNode.rightChild is None:

            rootNode.rightChild = BSTNode(nodeValue)

        else:

            insertNode(
                rootNode.rightChild,
                nodeValue
            )


# =========================================================
# Preorder Traversal
# Root -> Left -> Right
# =========================================================

def preOrderTraversal(rootNode):

    if not rootNode:
        return

    print(rootNode.data, end="  ")

    preOrderTraversal(rootNode.leftChild)

    preOrderTraversal(rootNode.rightChild)


# =========================================================
# Inorder Traversal
# Left -> Root -> Right
# =========================================================

def inOrderTraversal(rootNode):

    if not rootNode:
        return

    inOrderTraversal(rootNode.leftChild)

    print(rootNode.data, end="  ")

    inOrderTraversal(rootNode.rightChild)


# =========================================================
# Postorder Traversal
# Left -> Right -> Root
# =========================================================

def postOrderTraversal(rootNode):

    if not rootNode:
        return

    postOrderTraversal(rootNode.leftChild)

    postOrderTraversal(rootNode.rightChild)

    print(rootNode.data, end="  ")


# =========================================================
# Search Node Function
# =========================================================

def searchNode(rootNode, nodeValue):

    # Value not found
    if rootNode is None:

        print("\nValue not found")
        return

    # Value found
    if rootNode.data == nodeValue:

        print("\nThe value is found")
        return

    # Search left subtree
    elif nodeValue < rootNode.data:

        searchNode(
            rootNode.leftChild,
            nodeValue
        )

    # Search right subtree
    else:

        searchNode(
            rootNode.rightChild,
            nodeValue
        )


# =========================================================
# Driver Code
# =========================================================

newBST = BSTNode(None)

# Insert Nodes
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
insertNode(newBST, 10)

# Traversals
print("Preorder Traversal :")

preOrderTraversal(newBST)

print("\n\nInorder Traversal :")

inOrderTraversal(newBST)

print("\n\nPostorder Traversal :")

postOrderTraversal(newBST)

# Search Node
searchNode(newBST, 110)

print("\n")

print("\n" + "=" * 60 + "\n")


# =========================================================
# Summary of Concepts Practiced
# =========================================================
# ✔ Arrays
# ✔ Binary Tree
# ✔ Binary Search Tree
# ✔ BST Traversal
# ✔ Searching
# ✔ Functions
# ✔ Problem Solving
# =========================================================

print("Day 8 Part 1 Practice Completed Successfully 🚀")