# ============================================================
# Day 10 Part 2 - Python DSA Practice
# Author : Chitralekha Ghadge
# Topics : Graph using Adjacency Matrix and Hashing
# ============================================================


# ============================================================
# 1. Graph using Adjacency Matrix
# ============================================================

# Consider this graph:
#
#        A ----- B
#        |       |
#        |       |
#        C ----- D
#
# Connections:
# A <-> B
# A <-> C
# B <-> D
# C <-> D


print("1. Graph using Adjacency Matrix\n")


class Graph:

    def __init__(self, vertices):

        # Total number of vertices
        self.V = vertices

        # Create adjacency matrix with all 0 values
        self.matrix = [[0 for _ in range(vertices)]
                       for _ in range(vertices)]

    # Add edge between vertices
    def add_edge(self, u, v):

        self.matrix[u][v] = 1
        self.matrix[v][u] = 1      # Undirected Graph

    # Remove edge
    def remove_edge(self, u, v):

        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    # Display matrix
    def display(self):

        for row in self.matrix:
            print(row)


# Create graph with 4 vertices
g = Graph(4)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("Adjacency Matrix Before Removing Edge:")
g.display()

# Remove edge
g.remove_edge(0, 1)

print("\nAdjacency Matrix After Removing Edge (0,1):")
g.display()

print("\n" + "=" * 60)


# ============================================================
# 2. Introduction to Hashing
# ============================================================

# Hashing is a technique used to convert data
# into a fixed-size value called Hash Value.

# Advantages of Hashing:
# ✔ Fast Searching
# ✔ Fast Insertion
# ✔ Fast Deletion
# ✔ O(1) Average Time Complexity


print("\n2. Hashing Example\n")


class HashTable:

    def __init__(self, size):

        self.size = size

        # Create empty hash table
        self.table = [[] for _ in range(size)]

    # Hash Function
    def hash_function(self, key):

        return key % self.size

    # Insert data
    def insert(self, key):

        index = self.hash_function(key)

        self.table[index].append(key)

        print(f"{key} inserted at index {index}")

    # Display hash table
    def display(self):

        print("\nHash Table:")

        for i in range(self.size):

            print(i, "->", self.table[i])


# Create Hash Table
h = HashTable(10)

# Insert Elements
h.insert(15)
h.insert(25)
h.insert(35)
h.insert(42)
h.insert(52)

# Display Hash Table
h.display()

print("\n" + "=" * 60)


# ============================================================
# 3. Collision Example
# ============================================================

print("\n3. Collision in Hashing\n")

print("15 % 10 =", 15 % 10)
print("25 % 10 =", 25 % 10)
print("35 % 10 =", 35 % 10)

print("\nAll values stored at same index.")
print("This is called Collision.")

print("\n" + "=" * 60)


# ============================================================
# 4. Time Complexity of Hashing
# ============================================================

print("\n4. Time Complexity\n")

print("Operation      Without Hashing     With Hashing")
print("Search         O(n)                O(1)")
print("Insert         O(n)                O(1)")
print("Delete         O(n)                O(1)")

print("\n" + "=" * 60)


# ============================================================
# 5. Real World Applications of Hashing
# ============================================================

print("\n5. Real World Applications\n")

print("1. Google Search Engine")
print("2. Python Dictionary")
print("3. Database Indexing")
print("4. Password Security")
print("5. Caching Systems")

print("\n" + "=" * 60)


# ============================================================
# Simple Arithmetic Example
# ============================================================

print("\n6. Simple Arithmetic Example\n")

print("21 + 40 =", 21 + 40)

print("\n" + "=" * 60)


# ============================================================
# Summary
# ============================================================
# ✔ Graph using Adjacency Matrix
# ✔ Add Edge
# ✔ Remove Edge
# ✔ Display Matrix
# ✔ Hashing Concept
# ✔ Hash Function
# ✔ Collision Handling
# ✔ Hash Table Implementation
# ✔ Time Complexity
# ✔ Real World Applications
# ============================================================

print("\nDay 10 Part 2 Practice Completed Successfully 🚀")