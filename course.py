class Course:
    def __init__(self, course_name, available_seats):
        self.course_name = course_name
        self.available_seats = available_seats
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.available_seats:
            self.students.append(student)
            print(f"{student.name} added to {self.course_name}.")
        else:
            print(f"No more seats available for {student.name} in {self.course_name}.")

    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"{student_name} removed from {self.course_name}.")
                return
        print(f"Student {student_name} not found in {self.course_name}.")

    def calculate_average_score(self):
        if not self.students:
            return 0
        total_score = sum(student.lab_points + student.midterm_points + student.quiz_points + student.final_exam_points for student in self.students)
        return total_score / len(self.students)

    def determine_grade(self, student):
        score = student.lab_points + student.midterm_points + student.quiz_points + student.final_exam_points
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def print_student_grades(self):
        for student in self.students:
            grade = self.determine_grade(student)
            print(f"{student.name}'s grade: {grade}")

    def find_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.lab_points + student.midterm_points + student.quiz_points + student.final_exam_points)
