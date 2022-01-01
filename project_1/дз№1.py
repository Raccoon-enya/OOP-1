class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lc(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in lector.grades.keys():
            for grad in list(lector.grades[key]):
                sum = sum + grad
                len += 1
        lector.average_rating = round(sum / len, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнить')
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за домашние задания: {self.average_rating}\n'\
              f'Курсы в процессе изучения: {self.courses_in_progress}\n'\
              f'Завершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0
        self.students_list = []

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нельзя сравнить')
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за лекции: {self.average_rating}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in student.grades.keys():
            for grad in list(student.grades[key]):
                sum = sum + grad
                len += 1
        student.average_rating = round(sum / len, 2)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


one_student = Student('Дмитрий', 'Енин', 'муж')
one_student.finished_courses += ['Python']
one_student.courses_in_progress += ['Git']
one_student.courses_in_progress += ['Python']

two_student = Student('Лариса', 'Мищук', 'жен')
two_student.finished_courses += ['Python']
two_student.courses_in_progress += ['Python']
two_student.courses_in_progress += ['Git']

one_lecturer = Lecturer('Василий', 'Форточкин')
one_lecturer.courses_attached += ['Python']

two_lecturer = Lecturer('Аркадий', 'Паровозов')
two_lecturer.courses_attached += ['Git']

one_reviewer = Reviewer('Николай', 'Дроздов')
one_reviewer.courses_attached += ['Python']
one_reviewer.courses_attached += ['Git']

two_reviewer = Reviewer('Александр', 'Матросов')
two_reviewer.courses_attached += ['Python']

student_list = [one_student, two_student]
lecturer_list = [one_lecturer, two_lecturer]


def average_rating_hw(students, courses):
    sum_courses_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_courses_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_courses_grade / iterator, 2)


def average_rating_lesson(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


one_student.rate_lc(one_lecturer, 'Python', 8)
one_student.rate_lc(one_lecturer, 'Python', 9)
one_student.rate_lc(two_lecturer, 'Git', 7)
one_student.rate_lc(two_lecturer, 'Git', 6)

two_student.rate_lc(one_lecturer, 'Python', 8)
two_student.rate_lc(one_lecturer, 'Python', 9)
two_student.rate_lc(two_lecturer, 'Git', 5)
two_student.rate_lc(two_lecturer, 'Git', 7)

one_reviewer.rate_hw(one_student, 'Python', 8)
two_reviewer.rate_hw(one_student, 'Python', 8)
one_reviewer.rate_hw(one_student, 'Git', 6)
one_reviewer.rate_hw(one_student, 'Git', 7)
one_reviewer.rate_hw(two_student, 'Python', 7)
two_reviewer.rate_hw(two_student, 'Python', 6)
one_reviewer.rate_hw(two_student, 'Git', 6)
one_reviewer.rate_hw(two_student, 'Git', 7)

print('Список студентов:')
print(f'{one_student}\n')
print(f'{two_student}\n')
print('Список лекторов:')
print(f'{one_lecturer}\n')
print(f'{two_lecturer}\n')
print('Список проверяющих:')
print(f'{one_reviewer}\n')
print(f'{two_reviewer}\n')

print(f"Средняя оценка за дз у Енина больше, чем у Мищук {one_student > two_student}")
print(f"Средняя оценка за лекции у Форточкина меньше, чем у Паровозова {one_lecturer > two_lecturer}\n")

print(f'Средняя оценка студентов за курс GIT: {average_rating_hw(student_list, "GIT")}')
print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {average_rating_lesson(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {average_rating_lesson(lecturer_list, "GIT")}')
