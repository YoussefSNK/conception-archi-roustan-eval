class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grades = [grade1, grade2, grade3]

    def average(self):
        return sum(self.grades) / len(self.grades)


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_by_subject(self, subject_index):
        sorted_students = sorted(self.students, key=lambda s: s.grades[subject_index], reverse=True)
        print("Matière", subject_index+1)
        for student in sorted_students:
            print(f"  {student.name} : {student.grades[subject_index]}")

    def display_by_average(self):
        sorted_students = sorted(self.students, key=lambda s: s.average(), reverse=True)
        print("Moyenne :")
        for student in sorted_students:
            print(f"  {student.name} : {student.average():.2f}")
