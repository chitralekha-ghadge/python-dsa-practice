# ============================================================
# Day 9 Part 2 - Python DSA Practice
# Author : Chitralekha Ghadge
# Topics : Graph, OOP Concepts, Inheritance, Polymorphism
# ============================================================


# ============================================================
# 1. Graph Introduction
# ============================================================
# Graph consists of a finite set of vertices (nodes)
# and edges connecting those vertices.
#
# Types of Graph:
# 1. Directed Graph
# 2. Undirected Graph
# 3. Weighted Graph
# 4. Unweighted Graph
#
# Graph Implementations:
# 1. Adjacency Matrix
# 2. Adjacency List
# ============================================================

print("1. Graph using Adjacency List\n")


# ============================================================
# Adjacency List Implementation using Dictionary
# ============================================================

class Graph:

    def __init__(self):

        # Dictionary to store graph
        self.adjacency_list = {}

    # Add Vertex
    def add_vertex(self, vertex):

        if vertex not in self.adjacency_list:

            self.adjacency_list[vertex] = []

            return True

        return False

    # Add Edge
    def add_edge(self, vertex1, vertex2):

        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:

            # Undirected Graph
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

            return True

        return False

    # Display Graph
    def display(self):

        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    # Remove Edge
    def remove_edge(self, vertex1, vertex2):

        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:

            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)

            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

            return True

        return False

    # Remove Vertex
    def remove_vertex(self, vertex):

        if vertex in self.adjacency_list:

            for other_vertex in self.adjacency_list[vertex]:

                self.adjacency_list[other_vertex].remove(vertex)

            del self.adjacency_list[vertex]

            return True

        return False


# Create Graph Object
g = Graph()

# Add Vertices
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

# Add Edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")
g.add_edge("B", "E")
g.add_edge("C", "D")
g.add_edge("D", "E")

print("Graph Before Removing:")
g.display()

# Remove Vertex
g.remove_vertex("D")

print("\nGraph After Removing Vertex D:")
g.display()

print("\n" + "=" * 60)


# ============================================================
# 2. Static Method Example
# ============================================================

print("\n2. Static Method Example\n")


class Student:

    @staticmethod
    def get_personal_detail(firstname, lastname):

        print("Personal Detail :", firstname, lastname)

    @staticmethod
    def contact_detail(mobile_no, rollno):

        print("Contact Detail :", mobile_no, rollno)


Student.get_personal_detail("Chitralekha", "Ghadge")
Student.contact_detail(7447715468, 1001)

print("\n" + "=" * 60)


# ============================================================
# 3. Single Level Inheritance
# ============================================================

print("\n3. Single Level Inheritance\n")


class College:

    def college_name(self):

        print("College Name : Ramdeobaba University")


class StudentInfo(College):

    def student_info(self):

        print("Student Name : Chitralekha Ghadge")
        print("Branch       : MCA")


obj = StudentInfo()

obj.college_name()
obj.student_info()

print("\n" + "=" * 60)


# ============================================================
# 4. Multilevel Inheritance
# ============================================================

print("\n4. Multilevel Inheritance\n")


class CollegeData:

    def college_name(self):

        print("College Name : Ramdeobaba University")


class StudentData(CollegeData):

    def student_info(self):

        print("Student Name : Chitralekha Ghadge")
        print("Branch       : MCA")


class Exam(StudentData):

    def subject(self):

        print("Subjects:")
        print("1. DBMS")
        print("2. AI")
        print("3. Python")


obj = Exam()

obj.college_name()
obj.student_info()
obj.subject()

print("\n" + "=" * 60)


# ============================================================
# 5. Multiple Inheritance
# ============================================================

print("\n5. Multiple Inheritance\n")


class SubMarks:

    DBMS = 80
    AI = 75
    PR = 70
    OE = 85


class PracMarks:

    DBMSpract = 25


class Result(SubMarks, PracMarks):

    def total(self):

        if self.DBMS >= 40 and self.AI >= 40 and self.PR >= 40 and self.DBMSpract >= 20:

            print("Result : PASS")

        else:

            print("Result : FAIL")


obj = Result()

obj.total()

print("\n" + "=" * 60)


# ============================================================
# 6. Method Overriding
# ============================================================

print("\n6. Method Overriding\n")


class RBI:

    def education_loan(self):

        print("Education Loan ROI = 9%")


class SBI(RBI):

    def education_loan(self):

        print("Education Loan ROI = 10%")

        # Calling parent class method
        super().education_loan()


obj = SBI()

obj.education_loan()

print("\n" + "=" * 60)


# ============================================================
# 7. Constructor Overriding
# ============================================================

print("\n7. Constructor Overriding\n")


class Parent:

    def __init__(self):

        print("Parent Class Constructor")


class Child(Parent):

    def __init__(self):

        print("Child Class Constructor")

        # Calling Parent Constructor
        super().__init__()


obj = Child()

print("\n" + "=" * 60)


# ============================================================
# Summary
# ============================================================
# ✔ Graph using Adjacency List
# ✔ Static Methods
# ✔ Single Inheritance
# ✔ Multilevel Inheritance
# ✔ Multiple Inheritance
# ✔ Method Overriding
# ✔ Constructor Overriding
# ✔ OOP Concepts
# ✔ Polymorphism
# ============================================================

print("\nDay 9 Part 2 Practice Completed Successfully 🚀")