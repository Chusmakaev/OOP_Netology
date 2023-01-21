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

        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for q in self.grades:
            grades_count += len(self.grades[q])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
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
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        """self.name = name
        self.surname = surname
        self.courses_attached = []"""

        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        """Возвращает характеристики экземпляра класса вида:
            print(some_reviewer)
            Имя: Some
            Фамилия: Buddy
        """
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        #исключение пробелемы ZeroDivisionError
        try:
            self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        except ZeroDivisionError:
            grades_count = 0
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
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
best_lecturer_1 = Lecturer('Mr', 'Blaide')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Cap', 'America')
best_lecturer_2.courses_attached += ['Git']

best_lecturer_3 = Lecturer('Ghost', 'Rider')
best_lecturer_3.courses_attached += ['Java']

#Создаем список Проверяющих
cool_reviewer_1 = Reviewer('Peter', 'Parker')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Will', 'Smith')
cool_reviewer_2.courses_attached += ['Java']
cool_reviewer_2.courses_attached += ['Python']

cool_reviewer_3 = Reviewer('Dead', 'Shoot')
cool_reviewer_3.courses_attached += ['Java']
cool_reviewer_3.courses_attached += ['Python']


#Cоздаем список Менторов
cool_mentor_1 = Mentor('Bruce', 'Wane')
cool_mentor_1.courses_attached += ['Python']


cool_mentor_2 = Mentor('Robin', 'Gud')
cool_mentor_2.courses_attached += ['Java']

#Cоздаем список Студентов

best_student_1 = Student('Iron', 'man', '35')
best_student_1.finished_courses += ['Git']
best_student_1.courses_in_progress += ['Python']


best_student_2 = Student('Spider', 'man', '35')
best_student_2.finished_courses += ['Java']
best_student_2.courses_in_progress += ['Git']

best_student_3 = Student('Mr', 'Ravil', '26')
best_student_3.finished_courses += ['Git']
best_student_3.courses_in_progress += ['Java']

#Выставление оценок Студентам
best_student_1.grades ['Git'] = [10, 10, 10, 10, 10]
best_student_1.grades ['Python'] = [10, 10]

best_student_2.grades ['Git'] = [10, 10, 5, 5, 5]
best_student_2.grades ['Python'] = [10, 7]

best_student_3.grades ['Git'] = [10, 10, 10, 5, 5]
best_student_3.grades ['Python'] = [10, 7]

#Выставление оценок Лекторам
best_student_1.rate_hw(best_lecturer_1, 'Python', 10)
best_student_1.rate_hw(best_lecturer_1, 'Python', 6)
best_student_1.rate_hw(best_lecturer_1, 'Python', 5)


best_student_2.rate_hw(best_lecturer_2, 'Git', 7)
best_student_2.rate_hw(best_lecturer_2, 'Git', 10)
best_student_2.rate_hw(best_lecturer_2, 'Git', 8)

best_student_3.rate_hw(best_lecturer_3, 'Java', 7)
best_student_3.rate_hw(best_lecturer_3, 'Java', 6)
best_student_3.rate_hw(best_lecturer_3, 'Java', 8)

#Выставление оценок Студентам
cool_reviewer_1.rate_hw(best_student_1, 'Git', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Git', 3)
cool_reviewer_1.rate_hw(best_student_1, 'Git', 4)


cool_reviewer_2.rate_hw(best_student_2, 'Python', 5)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 6)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 9)

cool_reviewer_3.rate_hw(best_student_3, 'Python', 5)
cool_reviewer_3.rate_hw(best_student_3, 'Python', 6)
cool_reviewer_3.rate_hw(best_student_3, 'Python', 9)


print(f'Перечень студентов: \n\n{best_student_1}\n\n{best_student_2}\n\n{best_student_3}')
print()
print()

print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

print(f'Сравнение студентов:'
      f'{best_student_1.name} {best_student_1.surname} < {best_student_2.name} {best_student_2.surname} = {best_student_1 > best_student_2}')
print()

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

student_list = [best_student_1, best_student_2, best_student_3]

lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):
    """Функция для подсчета средней оценки за домашние задания
    по всем студентам в рамках конкретного курса
    в качестве аргументов принимает список студентов и название курса"""

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
     в качестве аргумента принимает список лекторов и название курса"""

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()



