### for loop###

# for i in range(1,5):
#    print("Hello World")

### while loop###

#i=1
#while i<=5:
#    print("Hello World")
 #   i+=1

### functions###

#def great():
#    print("Hello World")    
#    print("Welcome to Python Programming")
#great()

#def add(a,b):
#   result=a+b
#    print(result)
#add(20,50)
#add(25,73)

### lists###

#students=["Thanu","Ravi","Sita","Kiran"]
#print(students)
#students.append("Ramesh")
#print(students)
#students.remove("Ravi")
#print(students)
#students.insert(1,"Ravi")
#print(students)

###tuples###

#animals=("Dog","Cat","Cow","Lion")
#print(animals)

####dictionaries###

#student={"name":"Thanu","usn":"1GD24CS157","age":20,"marks":40}
#print(student)
#print(student["name"])

#Student={"COURSE":"python Programming","NAME":"Thanu","USN":"1GD24CS157","BRANCH":"CSE","SEMESTER":"5th"}
#print(Student)
#print(Student["COURSE"],Student["NAME"],Student["USN"],Student[ "BRANCH"],Student["SEMESTER"])

###classes and objects###

#class Student:
#   def display(self):
#        print("Hello World")
#        print("Welcome to Python Programming")
#s1=Student()
#s1.display()
##s1=self##


###constructor###

#class Student:
#    def __init__(self,name,usn,age,marks):
#        self.name=name
#        self.usn=usn
#        self.age=age
#        self.marks=marks
#    def display(self):
#        print("Name:",self.name)
#        print("USN:",self.usn)
#        print("Age:",self.age)
#       print("Marks:",self.marks)
#s1=Student("Thanu","1GD24CS157",20,40)
#s2=Student("Shree","1GD24CS141",21,50)
#s1.display()
#s2.display()


###encapsulation###


#class student:
#    def __init__(self):
#        self.__marks = 0

#    def set_marks(self, marks):
#        self.__marks = marks

#    def show_marks(self):
 #       print("Student Marks:", self.__marks)


#s1 = student()
#s1.set_marks(40)
#s1.show_marks()

####inheritance###

##multilevel inheritance##

# class grandfather:
#     def house(self):
#         print("grandfather has a house")
# class father(grandfather):
#     def car(self):
#         print("father has a car")
# class son(father):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.car() 
# s.bike()


##single inheritance##

# class father:
#     def car(self):
#         print("father has a car")
# class son(father):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.car()
# s.bike()

###multiple inheritance##

# class father:
#     def car(self):
#         print("father has a car")
# class mother:
#     def bike(self):
#         print("mother has a bike")
# class son(father,mother):
#     def house(self):
#         print("son has a house")
# s=son()
# s.car()
# s.bike()
# s.house()

##heirarchical inheritance##

# class father:
#     def car(self):
#         print("father has a car")
# class son(father):
#      def bike(self):
#         print("son has a bike")
# class daughter(father):
#      def house(self):
#         print("daughter has a house")
# s=son()
# s.car()
# s.bike()
# d=daughter()
# d.car()
# d.house()

####polymorphism###

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# animals=[Dog(),Cat(),Animal()]   
# for animal in animals:
#     animal.sound()

##abstract class##

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class upi(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")
class card(payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")
p1=upi()
p2=card()


p1.pay(100)
p2.pay(200)
