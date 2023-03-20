from enum import Enum
from uuid import UUID


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.alive = AliveStatus

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_DOB(self, new_dob):
        self.date_of_birth = new_dob

    def update_status(self, new_status):
        self.alive = new_status


class Instructor(Person):
    def _init__(self, first_name, last_name, date_of_birth, instructor_id):
        self.instructor_id = f'Instructor{instructor_id}{UUID()}'
        super.__init__(first_name,last_name,date_of_birth)

class Student(Person):

    def __init__(self, first_name, last_name, date_of_birth, student_id):
        super().__init__(first_name, last_name, date_of_birth)
        self.student_id = f'Student{student_id}{UUID()}'

class ZipCodeStudent(Student):
    def __int__(self, first_name, last_name, date_of_birth):
        super().__int__(first_name,last_name,date_of_birth)

class HighSchoolStudents(Student):
    def __int__(self, first_name, last_name, date_of_birth):
        super().__int__(first_name, last_name, date_of_birth)

class ClassRoom:

    def __int__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, new_instructor):
        self.instructors.append(new_instructor)

    def add_student(self, new_student):
        self.students.append(new_student)

    def remove_instructor(self, rm_instructor):
        self.instructors.remove(rm_instructor)

    def remove_student(self, rm_student):
        self.students.remove(rm_student)

    def print_instructor(self, instructor):
        print(self.instructors[instructor])

    def print_students(self, student):
        print(self.students[student])