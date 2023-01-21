class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        """print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за домашние задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Введение в программирование"""

        grades_num = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for q in self.grades:
            grades_num += len(self.grades[q])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_num
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
              f'Заверщенные курсы : {finished_courses_string}'
        return res
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение неккоректно')
            return
        return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.name = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        """self.name = name
        self.name = surname
        self.courses_attached = []"""

        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}
    def __str__(self):
        """print(some_lecturer)
        Имя: Some
        Фамилия: Buddy
        Средняя оценка за лекции: 9.9"""

        grades_num = 0
        for q in self.grades:
            grades_num += len(self.grades[q])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_num
        res = f'Имя : {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.name = surname
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
        """print(some_reviewer)
        Имя: Some
        Фамилия: Buddy"""
        res = f'Имя: {self.name}\ Фамилия: {self.surname}'


#Создаем список Лекторов
best_lecturer_1 = Lecturer('Iron', 'Man')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('We are', 'Venome')
best_lecturer_2.courses_attached += ['Java']

#Создаем список Проверяющих
cool_reviewer_1 = Reviewer('Peter', 'Parker')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Will', 'Smith')
cool_reviewer_2.courses_attached += ['Java']
cool_reviewer_2.courses_attached += ['Python']


#Cоздаем список Менторов
cool_mentor_1 = Mentor('Bruce', 'Wane')
cool_mentor_1.courses_attached += ['Python']


cool_mentor_2 = Mentor('Robin', 'Gud')
cool_mentor_2.courses_attached += ['Java']

#Cоздаем список Студентов

best_student_1 = Student('Iron', 'man', '35')
best_student_1.finished_courses += ['Git']
best_student_1.courses_in_progress += ['Python']


best_student_2 = Student('Iron', 'man', '35')
best_student_2.finished_courses += ['Java']
best_student_2.courses_in_progress += ['Python']

#Выставление оценок Студентам
best_student_1.grades ['Git'] = [10, 10, 10, 10, 10]
best_student_1.grades ['Python'] = [10, 10]

best_student_2.grades ['Git'] = [10, 10, 5, 5, 5]
best_student_2.grades ['Python'] = [10, 7]

#Выставление оценок Лекторам
best_student_1.rate_hw(best_lecturer_1, 'Git', 10)
best_student_1.rate_hw(best_lecturer_1, 'Git', 6)
best_student_1.rate_hw(best_lecturer_1, 'Git', 5)


best_student_2.rate_hw(best_lecturer_2, 'Java', 7)
best_student_2.rate_hw(best_lecturer_2, 'Java', 10)
best_student_2.rate_hw(best_lecturer_2, 'Java', 8)


#Выставление оценок Студентам
cool_reviewer_1.rate_hw(best_student_1, 'Git', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Git', 3)
cool_reviewer_1.rate_hw(best_student_1, 'Git', 4)


cool_reviewer_2.rate_hw(best_student_2, 'Python', 5)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 6)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 9)






