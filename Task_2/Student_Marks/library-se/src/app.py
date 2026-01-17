class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = None


class MarksSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if not student_id or not name:
            raise ValueError("Student ID and name are required")

        if student_id in self.students:
            raise ValueError("Student already exists")

        self.students[student_id] = Student(student_id, name)

    def add_marks(self, student_id, marks):
        if student_id not in self.students:
            raise KeyError("Student not found")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.students[student_id].marks = marks
