from course import Course
from utility import load_students_from_json

def distribute_students(courses, students):
    for student in students:
        assigned = False
        for course in courses:
            if len(course.students) < course.available_seats:
                course.add_student(student)
                assigned = True
                break
        if not assigned:
            print(f"No available course for student: {student.name}")

def calculate_course_statistics(courses):
    for course in courses:
        print(f"\n{course.course_name}:")
        print(f"Average score: {course.calculate_average_score()}")
        course.print_student_grades()
        top_student = course.find_top_student()
        if top_student:
            print(f"Top student: {top_student.name} with total points: {top_student.lab_points + top_student.midterm_points + top_student.quiz_points + top_student.final_exam_points}")
        print(f"Seats left: {course.available_seats - len(course.students)}")

courses = [
    Course("Python", 40),
    Course("Design Patterns", 15),
    Course("Calculus", 50)
]

students = load_students_from_json('students.json')

distribute_students(courses, students)

calculate_course_statistics(courses)
