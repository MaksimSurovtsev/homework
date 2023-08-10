class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_rating(self):
        average = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        return average
    def add(self, course_name, grade):
        if course_name not in self.grades:
            self.grades[course_name] = []
            self.grades[course_name].append(grade)
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
    def __lt__(self, other):
        return self.average_rating() < other.average_rating()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_rating(self):
        average = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        return average

    def __str__(self):
        return f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self.average_rating()}\n'
    def __lt__(self, other):
        return self.average_rating() < other.average_rating()

class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия:{self.surname}\n'
def average_rating_by_course(students, course):
    total_grades = []
    count = 0
    for student in students:
        if course in student.grades:
            total_grades += student.grades[course]
            count += len(student.grades[course])
    if count == 0:
        return 0
    average = sum(total_grades) / count
    return average

# Студенты
student_1 = Student('Семен', 'Семенов', 'Муж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в програмирование"]

student_2 = Student('Ирина', 'Иванова', 'Жен')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Введение в програмирование"]

# Лекторы
lecturer_1 = Lecturer('Петр', 'Синегубов')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Надежда', 'Надеждина')
lecturer_2.courses_attached += ['Python']

# Проверяющие
reviewer_1 = Reviewer('Алексей', 'Душнилов')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Тамара', 'Дудко')
reviewer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_1.rate_homework(student_1, 'Python', 10)
reviewer_1.rate_homework(student_1, 'Python', 9)
reviewer_1.rate_homework(student_1, 'Python', 7)

reviewer_2.rate_homework(student_2, 'Python', 10)
reviewer_2.rate_homework(student_2, 'Python', 9)
reviewer_2.rate_homework(student_2, 'Python', 9)

# Оценки лекторам
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 6)

student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Python', 6)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]
course = 'Python'
average_rating = average_rating_by_course(student_list, course)
print(f"Средняя оценка за домашние задания по курсу {course}: {average_rating}")
average_rating = average_rating_by_course(lecturer_list, course)
print(f"Средняя оценка за домашние задания по курсу {course}: {average_rating}")
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)



