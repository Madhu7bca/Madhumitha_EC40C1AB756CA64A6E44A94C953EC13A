class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name={self.name}, roll_number={self.roll_number}, cgpa={self.cgpa})"


def sort_students(student_list):
    # Sort the student list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


# Test the function
if __name__ == "__main__":
    # Sample student objects
    students = [
        Student("Alice", "S123", 3.8),
        Student("Bob", "S456", 3.5),
        Student("Charlie", "S789", 3.9),
    ]

    print("Original student list:")
    for student in students:
        print(student)

    sorted_students = sort_students(students)

    print("\nStudent list sorted by CGPA (descending):")
    for student in sorted_students:
        print(student)
