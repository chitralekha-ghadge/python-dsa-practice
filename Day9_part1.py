# ============================================================
# Day 9 Part 1 - Python DSA Practice
# Author : Chitralekha Ghadge
# Topics : Tree Traversal, Stack, Queue, Linked List
# ============================================================


# ============================================================
# 1. Tree: Preorder Traversal
# ============================================================
# Root -> Left -> Right
# ============================================================

print("1. Tree: Preorder Traversal\n")


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):

        if self.root is None:
            self.root = Node(val)

        else:
            current = self.root

            while True:

                if val < current.info:

                    if current.left:
                        current = current.left

                    else:
                        current.left = Node(val)
                        break

                elif val > current.info:

                    if current.right:
                        current = current.right

                    else:
                        current.right = Node(val)
                        break

                else:
                    break


def preOrder(root):

    if root is None:
        return

    # Print root
    print(root.info, end=" ")

    # Traverse left subtree
    preOrder(root.left)

    # Traverse right subtree
    preOrder(root.right)


tree = BinarySearchTree()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.create(value)

print("Preorder Traversal:")
preOrder(tree.root)

print("\n")
print("=" * 60)


# ============================================================
# 2. Tree: Inorder Traversal
# ============================================================
# Left -> Root -> Right
# ============================================================

print("\n2. Tree: Inorder Traversal\n")


def inOrder(root):

    if root is None:
        return

    # Traverse left subtree
    inOrder(root.left)

    # Print root
    print(root.info, end=" ")

    # Traverse right subtree
    inOrder(root.right)


print("Inorder Traversal:")
inOrder(tree.root)

print("\n")
print("=" * 60)


# ============================================================
# 3. Tree: Postorder Traversal
# ============================================================
# Left -> Right -> Root
# ============================================================

print("\n3. Tree: Postorder Traversal\n")


def postOrder(root):

    if root is None:
        return

    # Traverse left subtree
    postOrder(root.left)

    # Traverse right subtree
    postOrder(root.right)

    # Print root
    print(root.info, end=" ")


print("Postorder Traversal:")
postOrder(tree.root)

print("\n")
print("=" * 60)


# ============================================================
# 4. Stack Using Linked List
# ============================================================
# Stack follows LIFO (Last In First Out)
# Operations:
# Push
# Pop
# Peek
# ============================================================

print("\n4. Stack Using Linked List\n")


class StackNode:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class StackLinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):

        node = self.head

        while node:
            yield node
            node = node.next


class Stack:

    def __init__(self):
        self.linkedList = StackLinkedList()

    def __str__(self):

        values = [str(x.value) for x in self.linkedList]

        return "\n".join(values)

    # Check stack is empty or not
    def isEmpty(self):

        return self.linkedList.head is None

    # Push operation
    def push(self, value):

        node = StackNode(value)

        node.next = self.linkedList.head

        self.linkedList.head = node

    # Pop operation
    def pop(self):

        if self.isEmpty():
            return "Stack is Empty"

        nodeValue = self.linkedList.head.value

        self.linkedList.head = self.linkedList.head.next

        return nodeValue

    # Peek operation
    def peek(self):

        if self.isEmpty():
            return "Stack is Empty"

        return self.linkedList.head.value

    # Delete stack
    def delete(self):

        self.linkedList.head = None


# Driver Code
customStack = Stack()

customStack.push(10)
customStack.push(20)
customStack.push(30)

print("Stack Elements:")
print(customStack)

print("\nTop Element:")
print(customStack.peek())

print("\nPop Element:")
print(customStack.pop())

print("\nUpdated Stack:")
print(customStack)

print("\n")
print("=" * 60)


# ============================================================
# 5. Queue Using Linked List
# ============================================================
# Queue follows FIFO (First In First Out)
# Operations:
# Enqueue
# Dequeue
# Peek
# ============================================================

print("\n5. Queue Using Linked List\n")


class QueueNode:

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class QueueLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):

        currentNode = self.head

        while currentNode:
            yield currentNode
            currentNode = currentNode.next


class Queue:

    def __init__(self):
        self.linkedList = QueueLinkedList()

    def __str__(self):

        values = [str(x) for x in self.linkedList]

        return " -> ".join(values)

    # Check queue is empty or not
    def isEmpty(self):

        return self.linkedList.head is None

    # Enqueue operation
    def enqueue(self, value):

        newNode = QueueNode(value)

        if self.linkedList.head is None:

            self.linkedList.head = newNode
            self.linkedList.tail = newNode

        else:

            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    # Dequeue operation
    def dequeue(self):

        if self.isEmpty():
            return "Queue is Empty"

        tempNode = self.linkedList.head

        if self.linkedList.head == self.linkedList.tail:

            self.linkedList.head = None
            self.linkedList.tail = None

        else:

            self.linkedList.head = self.linkedList.head.next

        return tempNode

    # Peek operation
    def peek(self):

        if self.isEmpty():
            return "Queue is Empty"

        return self.linkedList.head

    # Delete queue
    def delete(self):

        self.linkedList.head = None
        self.linkedList.tail = None


# Driver Code
customQueue = Queue()

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)

print("Queue Elements:")
print(customQueue)

print("\nFront Element:")
print(customQueue.peek())

print("\nDequeue Element:")
print(customQueue.dequeue())

print("\nUpdated Queue:")
print(customQueue)

print("\n")
print("=" * 60)


# ============================================================
# Summary
# ============================================================
# ✔ Tree Traversals
# ✔ Binary Search Tree
# ✔ Stack using Linked List
# ✔ Queue using Linked List
# ✔ LIFO and FIFO Concepts
# ✔ Linked List Operations
# ✔ HackerRank Practice
# ============================================================

print("\nDay 9 Part 1 Practice Completed Successfully 🚀")