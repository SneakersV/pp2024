import math
import numpy as np
import pandas as pd

# Student mark management
class Student:
    def __init__(self,id,name,DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__marks = {}
        
    def set_mark(self,course,mark):
        # Use math module to round-down student scores to 1-digit decimal upon input, floor()
        if course in self.__marks:
            self.__marks[course].append(math.floor(mark*10)/10)
        else:
            self.__marks[course]=[math.floor(mark*10)/10]
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    def __str__(self):
        return f"{self.__id:<15}\t{self.__name:<30}\t{self.__DoB}"
               
class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.__name}"
    

def to_int(n):
    try:
        return int(n)
    except:
        print(f"Invalid. Please try a number!")

def no_student():
    n = to_int(input("Enter number of student: "))
    return n

def set_stu_in4(students, n):
    print(f"Enter information of {n} students:\n")
    for i in range(n):
        print(f"Student {i+1}")
        id = input("Student id: ")
        name = input("Student's name: ")
        DoB = input("DoB(DD-MM-YYYY): ")  
        students.append(Student(id,name,DoB))
        

def no_course():
    n = to_int(input("Enter number of course: "))
    return n
    
def set_course_in4(courses,n):
    print(f"Enter information of {n} course(s):\n")
    for i in range(0,n):
        print(f"Course {i+1}")
        id = input("course's id: ")
        name = input("course's name: ")
        courses.append(Course(id,name))
    
def get_marks_for_each_course(students, courses):
    if len(courses)==0:
        print("No course!")
    else:
        print("Select Course:")
        for i, course in enumerate(courses,start=1):
            print(f"{i}. {course.get_name()}")
        selected_course_index = to_int(input("Enter course number: ")) - 1
        selected_course = courses[selected_course_index].get_name()
        stu_id = input("Student ID to get mark: ")
        
        j=0
        while (j < len(students)):
            if students[j].get_id() == stu_id:
                try:
                    mark = float(input("Mark:"))
                    students[j].set_mark(selected_course,mark)
                    break
                except ValueError:
                    print("Invalid!")
                    continue
            j += 1
        if j > len(students):
            print("Cannot find student!")
            
def show_student(students):
    for student in students:
        print(student)
    
def show_marks(students,courses):
    if len(courses)==0:
        print("No course!")
    else:
        print(f"Course list")
        for i, course in enumerate(courses,start=1):
            print(f"{i}. {course.get_name()}")
        selected_course_index = to_int(input("Enter course number: ")) - 1
        selected_course = courses[selected_course_index]
        print(f"Showing marks for students in the course '{selected_course.get_name()}':")
        for student in students:
            if selected_course.get_name() in student.get_marks():
                marks = student.get_marks()[selected_course.get_name()]
                print(f"{student.get_id():<15}\t{student.get_name():<30}: ",end='')
                for i in range(0,len(marks)):
                    print(f"{marks[i]} ",end = '')
        
def show_GPA(students,courses):
    if len(courses)==0:
        print("No course!")
    else:
        print(f"Course list")
        for i, course in enumerate(courses,start=1):
            print(f"{i}. {course.get_name()}")
        selected_course_index = to_int(input("Enter course number: ")) - 1
        selected_course = courses[selected_course_index]
        print(f"Showing GPA for students in the course '{selected_course.get_name()}':")
        for student in students:
            if selected_course.get_name() in student.get_marks():
                marks = student.get_marks()[selected_course.get_name()]
                gpa = np.array(marks).mean()
                print(' '*48 + "GPA")
                print(f"{student.get_id():<15}\t{student.get_name():<30}: {math.floor(gpa*10)/10}")

def run():
    students = []
    courses = []
    student_nums = 0
    course_nums = 0
    
    while True:
        print("""
----------------------------------------
Choose option:
    1. Input number of students
    2. Input number of courses
    3. Input student's information
    4. Input course's information
    5. Input marks for each courses
    6. Show students
    7. Show marks
    8. Show GPA
    9. Exit""")
        option = input("Option: ")
        try:
            option = int(option)
        except:
            print(f"Invalid option. Please enter a number!")
            continue
        
        if option == 1:
            student_nums = no_student()
        elif option == 2:
            course_nums = no_course()
        elif option == 3:
            set_stu_in4(students,student_nums)
        elif option == 4:
            if course_nums==0:
                print("No course exists!")
            else:
                set_course_in4(courses,course_nums)
        elif option == 5:
            get_marks_for_each_course(students, courses)
        elif option == 6:
            if student_nums == 0:
                print(f"No student!")
            else: 
                show_student(students)
        elif option == 7:
            if course_nums == 0:
                print(f"No course exists!")
            else:
                show_marks(students, courses)
        elif option == 8:
            show_GPA(students,courses)
        elif option == 9: 
            break
        else:
            print(f"Invalid. Please try again!")


run()