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

    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.grades[0], reverse=True)
        print("Top matière 1 :")
        for student in sorted_students:
            print(student.name, student.grades[0])

    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.grades[1], reverse=True)
        print("Top matière 2 :")
        
        for student in sorted_students:
            print(student.name, student.grades[1])

    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.grades[2], reverse=True)
        print("Top matière 3 :")
        for student in sorted_students:
            print(student.name, student.grades[2])


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))
school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()