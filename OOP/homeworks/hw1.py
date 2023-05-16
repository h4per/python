class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    
    def introduce_myself(self):
        print(f"Full Name: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Married: {'Yes' if self.is_married else 'No'}")

me = Person("Сегизбаев Ислам", 16, False)
me.introduce_myself()



class Student(Person):
    def __init__(self, fullname, age, is_married, marks={}):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def introduce_myself(self):
        print(f"Full Name: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Married: {'Yes' if self.is_married else 'No'}")
        print(f"Marks: {self.marks}")

    def avg_marks(self):
        print("Средняя оценка:", sum(self.marks.values()) / len(self.marks))

me = Student("Сегизбаев Ислам", 16, False ,{"Матем": 4, "История": 5, "Англ": 2})
me.introduce_myself()
me.avg_marks()



class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        Person.__init__(self,fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def introduce_myself(self):
        print(f"Full Name: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Married: {'Yes' if self.is_married else 'No'}")
        print(f"Experience: {self.experience} years")
        print(f"Salary: {self.salary} soms")

    def salary_checker(self):
        base_salary = self.salary 
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * base_salary
            print("Зарплата в общем:" ,base_salary + bonus)
        else:
            print("Зарплата:" ,base_salary)

teacher = Teacher("Олег Лобацевич", 28, False, 8, 20000)
teacher.introduce_myself()
teacher.salary_checker()


def create_students():
    stud1 = Student("Олег Коффи", 15, False, {"химия": 2, "биология": 4, "история": 2})
    stud2 = Student("Ян Топлес", 18, True, {"матем": 4, "русский": 4, "кыргыз. яз": 2})
    stud3 = Student("Жаныш Тыныбеков", 16, False, {"литра": 4, "русский": 5, "кыргыз. яз": 3})
    return[stud1, stud2, stud3]

student_list = create_students()
for student in student_list:
    student.introduce_myself()
    print("\nОценки:")
    for subject, grade in student.marks.items():
        print(f"{subject}: {grade}")
    avg_mark = student.avg_marks()
    print(f"Средняя оценка: {avg_mark}\n")