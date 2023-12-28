class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lecture_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rate_from_student:
                lecturer.rate_from_student[course] += [grade]
            else:
                lecturer.rate_from_student[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rating(self):
        total = 0
        for list_rate in self.grades.values():
            for i in list_rate:
                total += i
            return total / len(list_rate)

    def _progress_course(self):
        str_ = []
        for course in self.courses_in_progress:
            str_.append(course)
        return ', '.join(str_)

    def _finish_course(self):
        str_ = []
        for course in self.finished_courses:
            str_.append(course)
        return ', '.join(str_)

    def __lt__(self, other):
        if self._average_rating() < other._average_rating():
            return self.name < other.name

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \n"
                f"Средняя оценка за лекции: {self._average_rating()} \n"
                f"Курсы в процессе изучение: {self._progress_course()} \n"
                f"Завершённые курсы: {self._finish_course()}")


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.rate_from_student = {}

    def _average_rating(self):
        total = 0
        for list_rate in self.rate_from_student.values():
            for i in list_rate:
                total += i
            return total / len(list_rate)

    def __lt__(self, other):
        if self._average_rating() < other._average_rating():
            return self.name < other.name

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \n"
                f"Средняя оценка за лекции: {self._average_rating()}")


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:

                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


def average_mark(student_list, course):
    total = 0
    count = 0
    for student in student_list:
        if course in student.grades:
            for i in student.grades[course]:
                total += i
                count += 1
    if count > 0:
        average = total / count
        return average
    else:
        return 'Нет студентов'


def average_mark_lectures(lectures_list, course):
    total = 0
    count = 0
    for lecturer in lectures_list:
        if course in lecturer.rate_from_student:
            for i in lecturer.rate_from_student[course]:
                total += i
                count += 1
    if count > 0:
        average = total / count
        return average
    else:
        return 'Нет лекторов'


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.finished_courses += ['Введение в программирование']
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.grades['Git'] = [7, 8, 9, 10, 9]
some_student.grades['Python'] = [10, 8, 9]

cool_student = Student('Taras', 'Melnik', 'your_gender')
cool_student.finished_courses += ['Введение в программирование']
cool_student.finished_courses += ['Git']
cool_student.courses_in_progress += ['Python']
cool_student.grades['Python'] = [9, 9, 9, 10, 10]

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

good_reviewer = Reviewer('Vasya', 'Pupkin')
good_reviewer.courses_attached += ['Git']

some_lecturer = Lecturer('Some', 'Baddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.rate_from_student['Python'] = [9, 10, 9, 8]

awesome_lecturer = Lecturer('Homer', 'Simpson')
awesome_lecturer.courses_attached += ['Git']
awesome_lecturer.rate_from_student['Git'] = [7, 6, 9, 9]

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_student.lecture_rate(awesome_lecturer, 'Git', 8)
cool_student.lecture_rate(some_lecturer, 'Python', 9)


print(good_reviewer)
print()
print(some_reviewer)
print()
print(awesome_lecturer)
print()
print(some_lecturer)
print()
print(some_student)
print()
print(cool_student)
print('Some' > 'Homer')
print('Taras' < 'Eman')
print(average_mark([cool_student, some_student], 'Python'))
print(average_mark_lectures([some_lecturer, awesome_lecturer], 'Git'))

