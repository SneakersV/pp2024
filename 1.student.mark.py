# Student mark management
def to_int(n):
    try:
        return int(n)
    except:
        print(f"Invalid. Please try a number!")

def no_student():
    n = to_int(input("Enter number of student: "))
    return n

def get_stu_in4(students):
    id = input("Student id: ")
    name = input("Student's name: ")
    DoB = input("DoB(DD-MM-YYYY): ")
    students.append({'id': id, 'name': name, 'DoB': DoB, 'marks': {}})

def no_course():
    n = to_int(input("Enter number of course: "))
    return n
    
def get_course_in4(courses):
    id = input("course's id: ")
    name = input("course's name: ")
    courses.append({'id': id, 'name': name})
    
def get_marks(students, courses):
    if len(courses)==0:
        print("No course!")
    else:
        print("Select Course:")
        for i, course in enumerate(courses,start=1):
            print(f"{i}. {course['name']}")
        selected_course_index = to_int(input("Enter course number: ")) - 1
        selected_course = courses[selected_course_index]
        stu_id = input("Student ID to get mark: ")
        if stu_id not in [student['id'] for student in students]:
            print("Cannot find student!")
        else:
            for student in students:
                if student['id']== stu_id:
                    try:
                        mark = float(input("Mark: "))
                    except:
                        print("Invalid!")
                        continue
                    student['marks'][selected_course['id']] = mark
    
def show_student(students):
    for student in students:
        print(f"{student['id']:<15}\t{student['name']:<30}\t{student['DoB']}")
    
def show_marks(students,courses):
    print(f"Course list")
    for i, course in enumerate(courses,start=1):
        print(f"{i}. {course['name']}")
    selected_course_index = to_int(input("Enter course number: ")) - 1
    selected_course = courses[selected_course_index]
    print(f"Showing marks for students in the course '{selected_course['name']}':")
    for student in students:
        if selected_course['id'] in student['marks']:
            print(f"{student['id']:<15}\t{student['name']:<30}\t{student['marks'][selected_course['id']]:.2f}")

    
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
    8. Exit""")
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
            print(f"Enter the information of {student_nums} students.")
            for i in range(0, student_nums):
                print(f"student {i+1}:")
                get_stu_in4(students)
        elif option == 4:
            if course_nums==0:
                print("No course exists!")
            else:
                for i in range(0, course_nums):
                    print(f"Course {i+1}:")
                    get_course_in4(courses)
        elif option == 5:
            get_marks(students, courses)
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
            break
        else:
            print(f"Invalid. Please try again!")

run()