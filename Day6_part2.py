# ==========================================
# Day 6 Python Practice Problems - Part 2
# Author: Chitralekha Ghadge
# Topics: Dictionary, OOPs, Linked List
# ==========================================


# =========================================================
# 1. Find All Duplicates in a List
# =========================================================
# Question:
# Write a function to find duplicate elements
# from a list.
# =========================================================

print("1. Find All Duplicates in a List\n")

numbers = [4, 3, 2, 7, 8, 2, 1, 5, 5]

count = {}
duplicates = []

# Count occurrences
for num in numbers:

    if num in count:
        count[num] += 1

    else:
        count[num] = 1

# Find duplicates
for key, value in count.items():

    if value > 1:
        duplicates.append(key)

print("Original List :", numbers)
print("Duplicate Elements :", duplicates)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 2. Sort Dictionary by Key or Value
# =========================================================

print("2. Sort Dictionary by Key or Value\n")

data = {"C": 3, "B": 2, "A": 1}

print("Original Dictionary :", data)

# Sort dictionary by key
ascending_key = dict(sorted(data.items()))

# Sort dictionary by value descending
descending_value = dict(
    sorted(data.items(), key=lambda item: item[1], reverse=True)
)

print("Ascending by Key :", ascending_key)
print("Descending by Value :", descending_value)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 3. Instance Variable Example
# =========================================================

print("3. Instance Variable Example\n")


class New:

    def __init__(self):

        self.a = 10


obj1 = New()
obj2 = New()
obj3 = New()

obj1.a = 20

print("obj1.a =", obj1.a)
print("obj2.a =", obj2.a)
print("obj3.a =", obj3.a)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 4. Static Variable Example
# =========================================================

print("4. Static Variable Example\n")


class Demo:

    a = 10

    def __init__(self):

        self.name = "Chitralekha"


obj1 = Demo()
obj2 = Demo()
obj3 = Demo()

Demo.a = 50

print("obj1.a =", obj1.a)
print("obj2.a =", obj2.a)
print("obj3.a =", obj3.a)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 5. Difference Between Static and Instance Variable
# =========================================================

print("5. Static vs Instance Variable\n")


class College:

    # Static Variable
    college_name = "Modern College"

    def __init__(self):

        # Instance Variable
        self.student_name = "Chitralekha Ghadge"


principal = College()
teacher = College()
accountant = College()

print("Before Changing Values:\n")

print("Principal  =", principal.college_name,
      "|", principal.student_name)

print("Teacher    =", teacher.college_name,
      "|", teacher.student_name)

print("Accountant =", accountant.college_name,
      "|", accountant.student_name)

# Change static variable
College.college_name = "HBD"

# Change instance variable
principal.student_name = "Chitra"

print("\nAfter Changing Values:\n")

print("Principal  =", principal.college_name,
      "|", principal.student_name)

print("Teacher    =", teacher.college_name,
      "|", teacher.student_name)

print("Accountant =", accountant.college_name,
      "|", accountant.student_name)

print("\n" + "=" * 60 + "\n")


# =========================================================
# 6. Linked List Implementation
# =========================================================
# Operations:
# 1. Add Node LinkedList
# 2. Add Node in Beginning
# 3. Add Node in Between
# 4. Add Node in End
# 5. Display Linked List
# =========================================================

print("6. Linked List Implementation\n")


# =========================================================
# Node Class
# =========================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


# =========================================================
# Linked List Class
# =========================================================

class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    # =====================================================
    # Add Node in Linked List
    # =====================================================

    def addNode(self, value):

        newNode = Node(value)

        # If linked list is empty
        if self.head is None:

            self.head = newNode
            self.tail = newNode

        else:

            self.tail.next = newNode
            self.tail = newNode

        print("Node added successfully")

    # =====================================================
    # Add Node at Beginning
    # =====================================================

    def addNodeBeginning(self, value):

        newNode = Node(value)

        # If linked list is empty
        if self.head is None:

            self.head = newNode
            self.tail = newNode

        else:

            newNode.next = self.head
            self.head = newNode

        print("Node added at beginning successfully")

    # =====================================================
    # Add Node in Between
    # =====================================================

    def addBetween(self, after_value, new_value):

        temp = self.head

        while temp is not None:

            if temp.data == after_value:

                newNode = Node(new_value)

                newNode.next = temp.next
                temp.next = newNode

                # Update tail if inserted at last
                if temp == self.tail:
                    self.tail = newNode

                print("Node inserted successfully")
                return

            temp = temp.next

        print("Value not found in Linked List")

    # =====================================================
    # Add Node at End
    # =====================================================

    def addEnd(self, value):

        self.addNode(value)

    # =====================================================
    # Display Linked List
    # =====================================================

    def displayNode(self):

        temp = self.head

        # If linked list is empty
        if temp is None:

            print("Linked List is Empty")

        else:

            while temp is not None:

                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")


# =========================================================
# Driver Code
# =========================================================

if __name__ == '__main__':

    obj = LinkedList()

    while True:

        print("\n========== Linked List Menu ==========")

        print("1.Add Node LinkedList")
        print("2.Add Node in Beginning")
        print("3.Add Node in Between")
        print("4.Add Node in End")
        print("5.Display Linked List")
        print("6.Exit")

        ch = int(input("Enter your choice: "))

        # =================================================
        # Add Node LinkedList
        # =================================================
        if ch == 1:

            value = int(input("Enter value for node: "))

            obj.addNode(value)

        # =================================================
        # Add Node in Beginning
        # =================================================
        elif ch == 2:

            value = int(input("Enter value for node: "))

            obj.addNodeBeginning(value)

        # =================================================
        # Add Node in Between
        # =================================================
        elif ch == 3:

            after_value = int(
                input("Insert node after value: ")
            )

            new_value = int(
                input("Enter new node value: ")
            )

            obj.addBetween(after_value, new_value)

        # =================================================
        # Add Node in End
        # =================================================
        elif ch == 4:

            value = int(input("Enter value for node: "))

            obj.addEnd(value)

        # =================================================
        # Display Linked List
        # =================================================
        elif ch == 5:

            print("\nLinked List Elements:\n")

            obj.displayNode()

        # =================================================
        # Exit
        # =================================================
        elif ch == 6:

            print("Program Ended Successfully")
            break

        # =================================================
        # Invalid Choice
        # =================================================
        else:

            print("Invalid Choice")

print("\n" + "=" * 60 + "\n")


# =========================================================
# Summary of Concepts Practiced
# =========================================================
# ✔ Dictionary
# ✔ Sorting
# ✔ OOP Concepts
# ✔ Instance Variable
# ✔ Static Variable
# ✔ Linked List
# ✔ Functions and Classes
# ✔ Menu Driven Programs
# =========================================================

print("Day 6 Part 2 Practice Completed Successfully 🚀")