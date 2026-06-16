# Animal class whith overriding speak()

class Animal:
    def speak(self):
        print("Animals sounds like")
class Dog(Animal):
    def speak(self):
        print("Dog sounds like Woof")
class Cat(Animal):
    def speak(self):
        print("Cat sounds like Meow")
class Elephant(Animal):
    def speak(self):
        print("Elephant sound like Trumpet")
class Lion(Animal):
    def speak(self):
        print("Lion sounds like Roars")
class Cow(Animal):
    def speak(self):
        print("Cow sounds like Moos")

sounds=[Animal(),Dog(),Cat(),Elephant(),Lion(),Cow()]
for sound in sounds:
     sound.speak()

#Area of shapes

class Shape:
    def __init__(self,color):
        self.color=color
    def area(self):
        print(" Areas of different shapes")
class Circle(Shape):
    def __init__(self,radius,color):
        super().__init__(color)
        self.radius=radius
    def area(self):
        result=3.14*self.radius*self.radius
        print(f"Area of Circle :{result}")
    def __str__(self):
        return f" Radius of Circle:{self.radius} | Color:{self.color}"
    
class Rectangle(Shape):
    def __init__(self,length,breadth,color):
        super().__init__(color)
        self.length=length
        self.breadth=breadth
    def area(self):
        result=self.length*self.breadth
        print(f"Area of Rectangle :{result}")
    def __str__(self):
        return f" Length :{self.length} | Breadth: {self.breadth} | Color:{self.color}"
    
class Square(Shape):
    def __init__(self,side,color):
        super().__init__(color)
        self.side=side
    def area(self):
        result=self.side*self.side
        print(f"Area of Square :{result}")
    def __str__(self):
        return f" Side :{self.side} | Color:{self.color}"
    
circle=Circle(5,"red")
rectangle=Rectangle(4,5,"blue")
square=Square(6,"green")

print()
print("Area of Shapes")
shapes=[circle,rectangle,square]
for shape in shapes:
    shape.area()

print()

print(str(circle))
print(str(rectangle))
print(str(square))


# Practice Question

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Student(person):
  def __init__(self,name,age,marks,grade):
    super().__init__(name,age)
    self.__marks=marks
    self.__grade=grade
  def get_marks(self):
    return self.__marks
  def set_marks(self,marks):
    if marks>100:
      print("Marks are in valid")
    elif marks<0:
      print("marks are in valid")
    else:
      self.__marks=marks
      print(f"Marks :{self.__marks}")
  def get_grade(self):
    return self.__grade
  def set_grade(self):
    if self.__marks>=90:
      print("A")
    elif self.__marks>=80:
      print("B")
    elif self.__marks>=70:
      print("C")
    elif self.__marks>=50:
      print("D")
    else:
      print("F")
  def __str__(self):
      return (f"Name :{self.name} | Age :{self.age} | Marks :{self.__marks} | Grade :{self.__grade}")
  def __repr__(self):
      return (f"Student(Name :{self.name} | Age :{self.age} | Marks :{self.__marks} | Grade :{self.__grade})")

class Teacher(person):
  def __init__(self,name,age,salary,subject):
    super().__init__(name,age)
    self.__salary=salary
    self.__subject=subject
  def get_salary(self):
    return self.__salary
  def get_subject(self):
    return self.__subject
  def __str__(self):
    return (f"Name :{self.name} | Age :{self.age} | Salary :{self.__salary} | Subject :{self.__subject}")
  def __repr__(self):
    return (f"Teacher(Name :{self.name} | Age :{self.age} | Salary :{self.__salary} | Subject :{self.__subject})")

class School:
  def __init__(self,school_name):
    self.school_name=school_name
    self.students=[]
    self.teachers=[]
  def add_student(self,student):
    self.students.append(student)
    print(f"{student.name} is joined in {self.school_name}")
  def add_teacher(self,teacher):
    self.teachers.append(teacher)
    print(f"{teacher.name} is joined in {self.school_name}")
  def assign_teacher(self,student,teacher):
    student.teacher=teacher
    print(f"{teacher.name} is assigend to {student.name}")
  def top_student(self):
    for student in self.students:
      if student.get_marks()>=85:
        print(f"{student.name} is top student")
      else:
        print(f"{student.name} is not top student")
  def show_all(self):
    for student in self.students:
      print(student)
    print()
    for teacher in self.teachers:
      print(teacher)

student1=Student("Surendra",21,87,"Btech")
student2=Student("Manvitha",20,80,"Btech")
student3=Student("Suri",21,85,"Btech")

teacher1=Teacher("Revathi",23,50000,"Maths")
teacher2=Teacher("Manasa",22,60000,"Pyhton")
teacher3=Teacher("Mohan",23,65000,"Java")


school=School("Gitam university")

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

print()

school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_teacher(teacher3)

print()

school.assign_teacher(student1,teacher1)
school.assign_teacher(student2,teacher2)
school.assign_teacher(student3,teacher3)

print()

school.top_student()

print()

school.show_all()

print()

print(str(student1))
print()
print(repr(student1))
