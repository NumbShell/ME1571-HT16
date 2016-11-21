

courses = []


class Course():

    def __init__(self, course):
        self.course =  course
        self.students = []


    def setStudent(self, students):
        self.students.append(students)


    def __str__(self):
        return self.course + ',' + ' Students: ' + str(self.students)


def create_course():
    done = False

    course = Course(input("Course "))
    print("Add Students, type done to save and exit")

    while not done:
        stud = input('')

        if stud != 'done':
            course.setStudent(stud)
        else:
            done = True

    courses.append(course)

create_course()

for c in courses:
    print(c)